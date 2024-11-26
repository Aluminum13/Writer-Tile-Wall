# Writer Tile Wall
## 简介
有位亲友写手在某次和我聊天的时候，说到想要个日历之类的东西可以登记每天写作的数量。他说之前在微博的写手bot曾经看到有人传播一个有类似功能的excel，但是有点麻烦和不美观。我当场就想到了Github的Contributions墙，并觉得市面上肯定有开源代码可以支持这种功能，扫描文件、统计并可视化。结果翻了一下发现，好像还真的没有找到非常适合完全不会编程的人开箱即用的。于是这两天上班之余摸了一个出来。

事实上任何会在一段较长时间内从事文字相关工作（哪怕是写论文等）的情况下都可能能用得上它。

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
    - 针对这一点，目前有很难两全的问题。主要是因为没有很好的方式仅依靠扫描来区分“重命名”和“移除”（GitHub自己也没有做到这一点）因为文件本身不会以任何形式存储它重命名自什么文件，**重命名和移除一个文件并新增一个文件是没有差别的**。
    - 目前的实现方式是统计所有文件的总字数，这种方式会导致如果将文件从目录中移除，当天的工作量就会异常地少。（即如果你删除了一个10000字的文件，即便你今天新写了8000字，仍然会被认为今天工作量是-2000）
    - 另一种可以采取的实现方式是记录上次扫描时每个文件的字数，在扫描时分别统计当前有的所有文件的字数的变化。这样能够自动地忽略掉移除文件的影响。但是重命名文件会导致字数异常地多。（即如果你重命名了一个10000字的文件，即便你今天一个字都没有写，仍然会被认为今天的工作量是10000）
- 适用于更多文件类型（很容易但是暂时没看出必要性）

## 已知bug
- 已知在系统默认字符编码方式不为GBK的情况下有可能会在安装时出现bug（一般国内购买的电脑不存在这个问题），这主要是由于在scripts_and_registry中试图打印中文导致的。一般可以通过手动运行scripts_and_registry.py解决。暂时没想到很完善的处理方式所以没有修改，如果有遇到此问题或者其他问题难以解决请单独咨询。