#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 11:00
# @Author  : Fred Yang
# @File    : pull_code.py
# @Role    : 02. 获取代码


import os
import sys
import fire
Base_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(Base_DIR)
from public import exec_shell
# from get_publish_info import get_publish_data


class PullCode(object):
    """
    通过git地址拉取代码
    首次： git clone
    存在： git fetch --all && git pull
    """

    def __init__(self, repository):
        self.repository = repository  # 代码仓库
        self.repo_name = self.repository.split('/')[-1].replace('.git', '')  # 仓库名字
        self.version_dir = os.path.join('/var/www/version/',self.repository.split('/')[-2])
        self.code_dir = os.path.join(self.version_dir, self.repo_name)

    def git_clone(self):
        """检测发布目录没有代码则进行git clone"""
        try:
            if not os.path.exists(self.code_dir):
                print('[INFO]: Start pulling a new codebase to {}'.format(self.code_dir))
                ### 克隆代码
                git_clone_cmd = 'mkdir -p {} ;cd {} && git clone {}'.format(self.version_dir, self.version_dir,
                                                                            self.repository)
                print('[CMD:] ', git_clone_cmd)
                git_clone_status, git_clone_output = exec_shell(git_clone_cmd)
                if git_clone_status == 0:
                    print('[Success]: git clone {} successfully...'.format(self.repository))
                else:
                    print('[Error]: git clone {} failed ...'.format(self.repository))
                    exit(404)
            else:
                print('[PASS]： The repository already exists, skip the clone and update directly')
        except Exception as e:
            print(e)

    def checkout_tag(self, git_tag):
        """切换分支"""
        git_fetch_cmd = 'cd {} && git fetch -t -p -f && git fetch --all'.format(self.code_dir)  # 更新代码
        git_checkout_cmd = 'cd {} && git clean -df  && git checkout {}'.format(self.code_dir, git_tag)  # 切换分支

        try:
            git_fetch_status, git_fetch_output = exec_shell(git_fetch_cmd)
            if git_fetch_status == 0:
                git_check_status, git_check_output = exec_shell(git_checkout_cmd)
                if git_check_status == 0:
                    print('[Success]: git checkout tag: {} successfully...'.format(git_tag))
                else:
                    print('[Error]: git checkout tag: {} failed ...'.format(git_tag))
                    exit(402)
            else:
                print('[Error]: git fetch failed ...')
                exit(403)
        except Exception as e:
            print(e)
            exit(-500)


def main(repository, git_tag):
    """
    :param flow_id: 订单ID
    :param git_tag: Git Tag名字
    :return:
    """
    print('[INFO]: 这部分是用来在构建机器上拉取代码，切换Tag操作')
    # data = get_publish_data(flow_id)  # 配置信息
    obj = PullCode(repository)  # 初始化类
    obj.git_clone()  # 克隆代码
    obj.checkout_tag(git_tag)  # 切换Tag


if __name__ == '__main__':
    fire.Fire(main)

###  python3 /home/dev/python_dev/codo-publish/k8s/pull_code.py  231 v0.20181226R1