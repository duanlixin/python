# 在view-ui目录下执行该文件
# 输入参数：数据源文件夹，1 213 204 217
# 输入参数：实验文件夹名字，例如：baiduASPT1S
# 输入参数：忽略文件夹名字，例如.svn
import os, shutil

# 当前系统路径分隔符
sep = os.sep
# 当前系统路径
cwd = os.getcwd()
# 线上文件夹 map
maps = {
    '1': '1' + sep + 'baiduASPT1S',
    '213': '213' + sep + 'baiduASPP213HS',
    '204': '204' + sep + 'baiduASPT204S',
    '217': '217' + sep + 'baiduASPT217S'
}
# 文件夹基础路径
basePath = cwd + sep + 'view-ui' + sep + 'conf'+ sep + 'template' + sep


# 文件夹基础路径 + 目标文件夹
def combinationPath(path):
    return basePath + path

def copySvn(path, src, dst, ignoreFolder):
    for root, dirs, files in os.walk(path):
        for dirname in dirs:
            if dirname == ignoreFolder:
                src1 = root + sep + dirname
                dst1 = (root + sep + dirname).replace(src , dst)
                print(src1, dst1)
                shutil.move(src1, dst1)

def exchange(templateFolder, laberyName, ignoreFolder):

    # 全流量模板文件夹路径
    soucrcePath = combinationPath(maps[templateFolder])
    # 小流量模板文件夹路径
    targetPath = combinationPath(templateFolder + sep + laberyName)
    # 临时文件夹路径
    tempPathS = combinationPath(templateFolder + sep + 'tempS')
    tempPathL = combinationPath(templateFolder + sep + 'tempL')

    shutil.copytree(soucrcePath, tempPathL, ignore=shutil.ignore_patterns(ignoreFolder))
    shutil.copytree(targetPath, tempPathS, ignore=shutil.ignore_patterns(ignoreFolder))

    copySvn(soucrcePath, maps[templateFolder], templateFolder + sep + 'tempS', ignoreFolder)
    copySvn(targetPath, templateFolder + sep + laberyName, templateFolder + sep + 'tempL', ignoreFolder)

    shutil.rmtree(soucrcePath)
    shutil.rmtree(targetPath)

    os.rename(tempPathS, soucrcePath)
    os.rename(tempPathL, targetPath)
    print ('***Congratulation,  DONE!***')
# 1 204 213 217
templateFolder = str(input())
# # 实验文件夹 
laberyName = str(input())
# # 忽略的文件夹
ignoreFolder = str(input())

exchange(templateFolder, laberyName, ignoreFolder)


