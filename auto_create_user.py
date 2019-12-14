import gitlab

url = 'http://xxxxxxx'  # gitlab安装地址
private_token = 'xxxxxxxxxxxxxx'  # gitlab 登录密钥 需自己设置

# 登录 获取gitlab操作对象gl
gl = gitlab.Gitlab(url, private_token)

# 获取第一页的用户列表 （返回[<User id:1>,<User id:2>]）
users = gl.users.list()
# 获取所有的用户列表
# users = gl.users.list(all=True)

# 创建用户
"""
常用参数：以下参数都可以使用user对象进行修改
email （必填）-电子邮件
username （必填）-用户名
name （必填）-名称
password （可选）-密码
can_create_group （可选）-用户可以创建组-正确或错误
skip_confirmation （可选）-跳过确认-正确或错误（默认）
external （可选）-将用户标记为外部用户-true或false（默认）
"""
user = gl.users.create({'email': 'qinsh@qq.com',
                        'password': 'qinsh123456',
                        'username': 'qinsh',
                        'name': '秦始皇'})

# 根据用户ID获取用户对象
# user = gl.users.get(1)
# 根据用户Git账号获取用户对象
# user = gl.users.list(username="qinsh")[0]

# 根据用户对象可以进行如下操作
username = user.username  # 获取用户Git账号
name = user.name  # 获取用户姓名
user_id = user.id  # 获取用户ID

# 修改用户属性
user.external = True  # 将用户标记为外部用户
user.save()

# 删除用户
gl.users.delete(user_id)  # 根据用户ID进行删除
user.delete()  # 根据用户对象直接进行删除

# Group
# 获取第一页的组列表 （返回[<Group id:1>,<Group id:2>]）
groups = gl.groups.list()
# 获取所有的组列表
# groups = gl.groups.list(all=True)

# 根据组ID获取组对象 group_id
group = gl.groups.get(1)
# 根据组名称获取组对象 group_name
# group = gl.groups.get("group_name")
# 获取组所在的项目
projects = group.projects.list()

# 创建组
group = gl.groups.create({'name': 'group1', 'path': 'group1'})

# 修改组信息
group.description = 'My awesome group'
group.save()

# 删除组
gl.groups.delete(1)  # 通过组ID进行删除
group.delete()  # 通过组对象直接删除

# 获取当前组的成员
members = group.members.list()
# members = group.members.all(all=True)
# 通过组成员ID获取组员member_id
# members = group.members.get(1)

# 添加一个成员到指定组
"""
GIT权限：
gitlab.GUEST_ACCESS = 10
gitlab.REPORTER_ACCESS = 20
gitlab.DEVELOPER_ACCESS = 30
gitlab.MAINTAINER_ACCESS = 40
gitlab.OWNER_ACCESS = 50
"""
member = group.members.create({'user_id': user_id,
                               'access_level': gitlab.GUEST_ACCESS})

# 修改组的权限
member.access_level = gitlab.DEVELOPER_ACCESS
member.save()
# or
member.access_level = 10
member.save()

# 将成员从某组移除
group.members.delete(1)  # 通过组成员ID进行移除member_id
member.delete()  # 通过组成员对象直接进行移除
