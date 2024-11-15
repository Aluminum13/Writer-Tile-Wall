# Writer Tile Wall
## 简介
有位亲友写手在某次和我聊天的时候，说到想要个日历之类的东西可以登记每天写作的数量。他之前在微博的写手bot曾经看到有人传播一个有类似功能的excel但是有点麻烦和不美观。我当场就想到了Github的Contributions墙，并觉得市面上肯定有大量的开源代码可以支持这种扫描文件统计并可视化吧。结果翻了一下发现，好像还真的没有找到非常适合文手（一般完全不会编程）开箱即用的。于是这两天上班之余摸了一个出来。

这个项目可以定期扫描你指定的文件夹（及其所有子目录）下的txt和word文档，并统计字数。以及可以以类似Github瓷砖墙的风格将近一年的数据绘制出来。

## 使用说明
见“使用说明”目录下的“使用说明.txt”。

在使用中遇到任何问题均可以通过issue向作者提问。

## 开发计划
虽然仍然不甚美观以及不够完善，但已经姑且能用了，暂无继续开发的计划。如果有朋友有意开发欢迎加入并提交pull request。

已知至少可以完善的部分：
- 美化可视化
- 编写一个更傻瓜式和好看的GUI
- 不是通过统计字数差异而是通过编辑距离等方式来更好更完善地评估工作量。
