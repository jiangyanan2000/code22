"""
目标
·了解面向对象开发过程中类内部功能的分析方法
·了解常用系统功能
增加
删除
修改
查询
一、系统需求
使用面向对象思想完成学员管理系统的开发，需求如下：
·系统要求：学员数据存储在文件中
·系统功能：添加学员、删除学员、修改学员信息、查询学员信息，显示所有学员信息、保存学员信息及退出系统等功能
二、准备程序文件
2.1分析
·角色分析
    学员
    管理系统
工作中注意事项
1、为了方便维护代码，一般一个角色一个程序文件
2、项目要有主程序入口，习惯为main.py
2.2创建程序文件
创建项目目录，例如：StudentMangerSystem
三、书写程序
3.1 student.py
需求：
·学员信息包括：姓名，性别，手机号
·添加__str__方法，方便查看学员信息
3.2 managerSystem.py
需求：
·存储数据的位置：文件（student.data)
  加载文件数据
  修改数据后保存到文件
·存储数据的形式：列表存储学员对象
·系统功能
  添加学员
  删除学员
  修改学员
  查询学员信息
  显示所有学员信息
  保存学员信息
3.2.2管理系统框架
需求：系统循环使用，用户输入不同的功能序号执行不同的功能
·步骤
  定义程序入口程序
      显示功能菜单
      用户输入功能序号
      根据用户输入的功能序号执行不同的功能
  定义系统函数，添加，删除学员等

"""