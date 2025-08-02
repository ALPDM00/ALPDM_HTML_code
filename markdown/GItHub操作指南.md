# ============== 初始化仓库 ==============
# 本地创建新仓库
mkdir project_name
cd project_name
git init
git remote add origin https://github.com/username/repo.git

# 克隆现有仓库
git clone https://github.com/username/repo.git
cd repo

# ============== 日常操作 ==============
# 添加文件
git add filename.py  # 添加单个文件
git add .            # 添加所有新文件和修改

# 提交更改
git commit -m "描述您的更改"

# 推送到 GitHub
git push -u origin main  # 首次推送
git push                 # 后续推送

# 从 GitHub 拉取更新
git pull origin main

# ============== 分支管理 ==============
git checkout -b feature-branch  # 创建新分支
git checkout main               # 切换分支
git merge feature-branch        # 合并分支

# ============== 解决冲突 ==============
# 1. 编辑冲突文件（移除 <<<<<<<, =======, >>>>>>> 标记）
# 2. 标记冲突已解决
git add conflicted_file.py
git commit -m "解决合并冲突"

# ============== 最佳实践 ==============
# 创建 .gitignore 文件
echo "__pycache__/" >> .gitignore
echo "*.log" >> .gitignore
echo ".DS_Store" >> .gitignore
git add .gitignore
git commit -m "添加 .gitignore 文件"

# 常用命令速查
git status         # 查看当前状态
git log --oneline  # 查看提交历史
git diff           # 查看未暂存的更改
git restore <file> # 丢弃工作区更改
git remote -v      # 查看远程仓库信息