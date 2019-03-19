// HuaweiCar.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include "pch.h"
#include <iostream>
#define RoadNum 24
#define CarNum 9
#define CrossNum 16
using namespace std;

int Road[RoadNum][8] =  //#(道路id，道路长度，最高限速，车道数目，起始点id，终点id，是否双向)
{ { 501, 10, 6, 5, 1, 2, 1 },
{ 502, 10, 6, 5, 2, 3, 1 },
{ 503, 10, 6, 5, 3, 4, 1 },
{ 504, 10, 6, 5, 5, 6, 1 },
{ 505, 10, 6, 5, 6, 7, 1 },
{ 506, 10, 6, 5, 7, 8, 1 },
{ 507, 10, 6, 5, 9, 10, 1 },
{ 508, 10, 6, 5, 10, 11, 1 },
{ 509, 10, 6, 5, 11, 12, 1 },
{ 510, 10, 6, 5, 13, 14, 1 },
{ 511, 10, 6, 5, 14, 15, 1 },
{ 512, 10, 6, 5, 15, 16, 1 },
{ 513, 10, 6, 5, 1, 5, 1 },
{ 514, 10, 6, 5, 2, 6, 1 },
{ 515, 10, 6, 5, 3, 7, 1 },
{ 516, 10, 6, 5, 4, 8, 1 },
{ 517, 10, 6, 5, 5, 9, 1 },
{ 518, 10, 6, 5, 6, 10, 1 },
{ 519, 10, 6, 5, 7, 11, 1 },
{ 520, 10, 6, 5, 8, 12, 1 },
{ 521, 10, 6, 5, 9, 13, 1 },
{ 522, 10, 6, 5, 10, 14, 1 },
{ 523, 10, 6, 5, 11, 15, 1 },
{ 524, 10, 6, 5, 12, 16, 1 } };
int Car[CarNum][6] =//#(id,始发地,目的地,最高速度,出发时间)
{ {1001, 1, 16, 6, 1},
{1002, 2, 16, 6, 1},
{1003, 6, 16, 6, 1},
{1004, 9, 16, 6, 1},
{1005, 15, 16, 6, 1},
{1006, 1, 16, 6, 1},
{1007, 1, 16, 6, 1},
{1008, 1, 16, 6, 1} };
int Cross[CrossNum][6] = //#(结点id,道路id,道路id,道路id,道路id)
{{1, 501, 513, -1, -1},
{2, 501, -1, 502, 514},
{3, 502, -1, 503, 515},
{4, 503, -1, -1, 516},
{5, 513, 504, 517, -1},
{6, 504, 514, 505, 518},
{7, 505, 515, 506, 519},
{8, 506, 516, -1, 520},
{9, 517, 507, 521, -1},
{10, 507, 518, 508, 522},
{11, 508, 519, 509, 523},
{12, 509, 520, -1, 524},
{13, 521, 510, -1, -1},
{14, 510, 522, 511, -1},
{15, 511, 523, 512, -1},
{16, 512, 524, -1, -1}};

int findCar(int Carid)
/*输入Car的id，输出该id所在Car数组的行数，否则返回-108*/
{
	for (int i = 0; i < CarNum; i++)
	{
		if (Car[i][0] == Carid)
			return i;
	}
	return -108;
}
int findCrossResult[2];
void findCross_of_Road(int Roadid)/*Input 1 road id ,Output 2 cross id*/
/*输入1个Road的id，输出与该Road连接的2个Cross的id（必定是2个）
结果存放于findCrossResult数组中，数组内值即为Cross的id，若为-101说明Roadid不在Road数据中
findCrossResult数组中的数据乱序，
*/
{
	for (int i = 0; i < RoadNum; i++)
	{
		if (Road[i][0] == Roadid)
		{
			findCrossResult[0] = Road[i][4];
			findCrossResult[1] = Road[i][5];
			return;
		}
	}
	findCrossResult[0] = -101;
	findCrossResult[1] = -101;//unfind
	//可直接通过Road[id-5000][4],Road[id-5000][5]或Road[id-5001][4],Road[id-5001][5]得到
}

int findRoadResult[4];
void findRoad_of_Cross(int Crossid)//给定一条路口id，给出1-4个道路id
/*输入1个Cross的id，输出与该Cross相连接的1至4个Road的id（数量不定）
结果存放于findRoadResult数组中，数组内值即为Road的id，若为-102说明Crossid不在Cross数据中；存在几个-1则说明该Cross在最多连接4个Road的基础上少几个
findRoadResult数组中的数据乱序，若存在-1则其所在位置随机*/
{
	for (int i = 0; i < CrossNum; i++)
	{
		if (Cross[i][0] == Crossid)
		{
			for(int j=0;j<4;j++)
			{
			findRoadResult[j]=Cross[i][j+1];
			}
			return;
		}
	}
	for (int j = 0; j < 4; j++)//unfind
	{
		findRoadResult[j] = -102;
	}
	//可以直接通过Road[id-1][1~4]得到
}

int BesideCrossRusult[4];
void BesideCross_of_Cross(int Crossid)	
/*输入Cross的id，输出与该Cross相邻的1~4个Cross的id（数量不定）
结果存放于BesideCrossRusult数组中，数组内值即为Cross的id，存在几个-103则说明该Cross在最多4个相邻Cross的基础上少几个
BesideCrossRusult数组中的数据乱序，若存在-103则其所在位置随机*/
/*
不考虑单行的情况
*/
{

	int RoadBesideCross[4];
	findRoad_of_Cross(Crossid);
	memcpy(RoadBesideCross, findRoadResult, sizeof(findRoadResult));//先获取Cross相邻的Road
	for (int i = 0; i < 4; i++)
	{
		if (RoadBesideCross[i] != -1)
		{
			findCross_of_Road(RoadBesideCross[i]);
			BesideCrossRusult[i] = findCrossResult[0] == Crossid ? findCrossResult[1] : findCrossResult[0];
		}
		else
		{
			BesideCrossRusult[i] = -103;
		}
	}
}

int BesideRoadResult[6];
void BesideRoad_of_Road(int Roadid)
/*输入Road的id，输出与该Road相邻的1~6个Road的id（数量不定）
结果存放于BesideCrossRusult数组中，数组内值即为Road的id，存在几个-1则说明该Road在最多6个相邻Road的基础上少几个
BesideCrossRusult数组中的数据乱序，若存在-1则其所在位置随机*/
/*
不考虑单行的情况
*/
{
	int CrossBesideRoad[2];
	findCross_of_Road(Roadid);
	memcpy(CrossBesideRoad, findCrossResult, sizeof(findCrossResult));//先获取Road相邻的Cross
	for (int i = 0; i < 2; i++)
	{
		findRoad_of_Cross(CrossBesideRoad[i]);
		int num = 0;
		for (int j = 0; j < 4; j++)
		{
			if (findRoadResult[j] != Roadid)
			{
				BesideRoadResult[num + i * 3] = findRoadResult[j];//每个Cross最多有3个Road（不含本身的Roadid）
				num++;
			}
		}
	}
}


int ifCrossAccess(int Cross1, int Cross2)//Input 2 Corss id , Output true/false  
/*输入两个Cross的id(有先后顺序)，判断Cross1和Cross2是否相邻(或从Cross1到Cross2是否可达)
输出为1说明相邻（即Cross1到Cross2之间有一条路）；
输出为0则说明Cross1到Cross2之间有一个Road，但路是单行导致从Cross1到Cross2不能通过该Road可达；
输出为-1说明Cross1到Cross2之间不存在一个Road相连接*/
{
	//if (Cross1 > Cross2) { int temp = Cross2; Cross2 = Cross1; Cross1 = temp; }
	for (int i = 0; i < RoadNum; i++)
	{
		if (Cross1 == Road[i][4] && Cross2 == Road[i][5])
		{
			if (Road[i][6] == 1)
			{
				return 1;//yes
			}
			else
			{
				return 1;//在单行时也可以
			}
		}
		else if (Cross1 == Road[i][5] && Cross2 == Road[i][4])
		{
			if (Road[i][6] == 1)
			{
				return 1;//yes
			}
			else
			{
				return 0;//在单行时no
			}
		}
	}
	{/*Road.txt后三项为 5 6 1时
	 intput 5 6  output ->yes
			6 5           yes
		5 6 0
	 intput 5 6  output ->yes
			6 5           no
		6 5 1
	 intput 5 6  output ->yes
			6 5           yes
		6 5 0
	 intput 5 6  output ->no
			6 5           yes
	 */
	}
	return -1;//un connected	
}

int ifRoadAccess(int Road1, int Road2)//Input 2 Road id , Output ture/false 判断两个Road是否相邻，如果是单行则需要进一步判断
/*输入两个Road的id(有先后顺序)，判断Road1和Road是否相邻(或可从Road1通过到Road2)
输出为1说明相邻（即Road1和Road2连接同一个Cross）；
输出为0则说明Road1和Road2连接同一个Cross，但Road1和Road2中存在有路是单行导致从Road1一端到该Cross再到Road2另一端不能通过；
输出为-1说明Road1和Road2没有连接同一个Cross*/
/*
以“十”举例，中间为Cross，分为上下左右四条路，参照下面注释和void testifRoadAccess_WhenBeside()
*/
{
	int Road1Access[2], Road2Access[2];
	findCross_of_Road(Road1);
	memcpy(Road1Access, findCrossResult, sizeof(findCrossResult));
	findCross_of_Road(Road2);
	memcpy(Road2Access, findCrossResult, sizeof(findCrossResult));
	if (Road1Access[0] == Road2Access[0])
	{
		if (ifCrossAccess(Road1Access[1], Road1Access[0]) == 1 && ifCrossAccess(Road2Access[0], Road2Access[1]) == 1)//order! “十” Road1在右，Road2在下，Road1通过Road路线为 右→中→下，即“┌”。或1为下，2为右，“┌”
		{
			//cout << "一";
			return 1;//yes
		}
		else
		{
			//cout << "二";
			return 0;//在单行时no
		}
	}
	else if (Road1Access[0] == Road2Access[1])
	{
		if (ifCrossAccess(Road1Access[1], Road1Access[0]) == 1 && ifCrossAccess(Road2Access[1], Road2Access[0]) == 1)//order “十” Road1在右，Road2在上（左），Road1通过Road路线为 右→中→上（左），即“└（─）“。或1为下，2为左（上），“┐（│）”
		{
			//cout << "三";
			return 1;//yes
		}
		else
		{
			//cout << "四";
			return 0;//在单行时no
		}
	}
	else if (Road1Access[1] == Road2Access[0])
	{
		if (ifCrossAccess(Road1Access[0], Road1Access[1]) == 1 && ifCrossAccess(Road2Access[0], Road2Access[1]) == 1)//order “十” Road1在左，Road2在下（右），Road1通过Road路线为 左→中→下（右），即“┐（─）”。或1为上，2为右（下），”└（│）“
		{
			//cout << "五";
			return 1;//yes
		}
		else
		{
			//cout << "六";
			return 0;//在单行时no
		}
	}
	else if (Road1Access[1] == Road2Access[1])
	{
		if (ifCrossAccess(Road1Access[0], Road1Access[1]) == 1 && ifCrossAccess(Road2Access[1], Road2Access[0]) == 1)//order “十” Road1在左，Road2在上，Road1通过Road路线为 左→中→上，即“┘”。或1为上，2为左，“┘”
		{
			//cout << "七";
			return 1;//yes
		}
		else
		{
			//cout << "八";
			return 0;//在单行时no
		}
	}
	else {
		return -1;//un connected
	}
}
/*
void testifRoadAccess_WhenBeside()
{
	//1为左，2为上右下
	cout << ifRoadAccess(505, 515) << " ";
	cout << ifRoadAccess(505, 506) << " ";
	cout << ifRoadAccess(505, 519) << endl;
	//1为上，2为右下左
	cout << ifRoadAccess(515, 506) << " ";
	cout << ifRoadAccess(515, 519) << " ";
	cout << ifRoadAccess(515, 505) << endl;
	//1为右，2为下左上
	cout << ifRoadAccess(506, 519) << " ";
	cout << ifRoadAccess(506, 505) << " ";
	cout << ifRoadAccess(506, 515) << endl;
	//1为下，2为左上右
	cout << ifRoadAccess(519, 505) << " ";
	cout << ifRoadAccess(519, 515) << " ";
	cout << ifRoadAccess(519, 506) << endl;
}*/



int findRoad_of_2Cross(int Cross1, int Cross2)
/*输入两个Cross的id，输出与这两个Cross都相连的Road，否则输出-105
*/
{
	for (int i =0;i<RoadNum;i++)
	{
		if (Road[i][4] == Cross1 && Road[i][5] == Cross2)
		{
			return Road[i][0];
		}
		else if (Road[i][5] == Cross1 && Road[i][4] == Cross2)
		{
			return Road[i][0];
		}
	}
	return -105;//unfind
}

int map[100][100];
void InitMap()
{
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			map[i][j] = 999;//最大值
}
void buildMap(int Carid)
{
/*	for (int i = 0; i < CrossNum; i++)
	{
		for (int j = i + 1; j < CrossNum; j++)//遍历 j<=?
		{
			if (findRoad_of_2Cross(i, j) > 0)//两条路相连
			{
				cout << i << "和" << j << "相连" << endl;
			}
		}
	}没必要*/
	InitMap();
	for (int i = 0; i < RoadNum; i++)
	{
		map[Road[i][4]][Road[i][5]] = Road[i][2] > Car[findCar(Carid)][3] ? Car[findCar(Carid)][3] : Road[i][2];
		//赋值构造map，如果车速小于道路最高速度则为道速最高速
		if (Road[i][6] == 1)//双向
		{
			map[Road[i][5]][Road[i][4]] = Road[i][2] > Car[findCar(Carid)][3] ? Car[findCar(Carid)][3] : Road[i][2];
		}
	}
}
void printMap()
{
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			if (map[i][j] != 999)
				cout << "map[" << i << "][" << j << "]=" << map[i][j] << endl;
}

int alreadygo[10000];//记录已经去过的路口
int alreadynum = 0;//记录已经去过的路口的数目
int alreadyfind = 0;//记录是否已经到过终点
void xunhuan(int Crossid,int endCross)
{
	alreadygo[alreadynum] = Crossid;
	alreadynum++;
	int findCResult[4];
	BesideCross_of_Cross(Crossid);
	memcpy(findCResult, BesideCrossRusult, sizeof(BesideCrossRusult));
	for (int i=0;i<4;i++)
	{
		for (int j = 0; j < alreadynum; j++)
		{
			if (findCResult[i] == alreadygo[j])
				findCResult[i] = -107;
		}
	}
/*	cout << "Already有";
	for (int i = 0; i < alreadynum + 10; i++)
	{
		cout << alreadygo[i]<<",";
	}*/
	/*
	cout << "针对Cross" << Crossid << "的相邻的是";
	for (int i : findCResult)
	{
		if(i > 0)
			cout << i<<" ";
	}
	cout << "/"<<endl;*/

	for (int i : findCResult)
	{
		if (i > 0)
		{
			cout << i << " ";
			if (i == endCross)//到了终点
			{

				cout<<" -"<<findRoad_of_2Cross(i, Crossid)<<"- ";
				//加入到走法
				alreadyfind = 1;

				return;
			}
			else if(alreadyfind==0)
			{
				xunhuan(i, endCross);
				//cout << " +" << findRoad_of_2Cross(i, Crossid) << "+ ";
			}
		}
	}
}
void findRoadend()
/*清空关于already数组与相关值的数据*/
{
	for (int i = 0; i < alreadynum; i++)
	{
		alreadygo[i]=-104;
	}
	alreadynum = 0;
	alreadyfind = 0;
}
int findRoad(int carid)
/*
输入车辆id，输出车辆id，出发时间，Road的id
*/
{
	int startCross, endCross,carSpeed;
	startCross = Car[carid - 1001][1];
	endCross = Car[carid - 1001][2];
	carSpeed = Car[carid - 1001][3];
	cout << "car " << carid << " ,startC " << startCross << " Road" << endl;
	xunhuan(startCross, endCross);
	findRoadend();
	cout << endl;
	return 0;
}
void TestCase1()
{

	findCross_of_Road(506);
	for (int i = 0; i < 2; i++)
	{
		cout << findCrossResult[i] << " ";
	}
	cout << endl;

	findRoad_of_Cross(6);
	for (int j = 0; j < 4; j++)
	{
		cout << findRoadResult[j] << " ";
	}
	cout << endl;
	cout << "ifCrossAccess" << endl;
	cout << ifCrossAccess(6, 2) << " ";
	cout << ifCrossAccess(6, 5) << " ";
	cout << ifCrossAccess(6, 7) << " ";
	cout << ifCrossAccess(6, 10) << " ";
	cout << ifCrossAccess(6, 12) << " ";
	cout << ifCrossAccess(6, 15) << " ";
	cout << ifCrossAccess(7, 6) << " ";
	cout << endl;

	cout << endl;
	cout << "ifRoadAccess" << endl;
	cout << ifRoadAccess(505, 504) << " ";
	cout << ifRoadAccess(505, 514) << " ";
	cout << ifRoadAccess(505, 518) << " ";
	cout << ifRoadAccess(505, 515) << " ";
	cout << ifRoadAccess(505, 506) << " ";
	cout << ifRoadAccess(505, 519) << " ";
	cout << ifRoadAccess(505, 508) << " ";
	cout << ifRoadAccess(505, 524) << " ";
	cout << endl;
	cout << ifRoadAccess(504, 505) << " ";
	cout << ifRoadAccess(514, 505) << " ";
	cout << ifRoadAccess(518, 505) << " ";
	cout << ifRoadAccess(515, 505) << " ";
	cout << ifRoadAccess(506, 505) << " ";
	cout << ifRoadAccess(519, 505) << " ";
	cout << ifRoadAccess(508, 505) << " ";
	cout << ifRoadAccess(524, 505) << " ";

	cout << endl;
	BesideCross_of_Cross(5);
	for (int j = 0; j < 4; j++)
	{
		cout << BesideCrossRusult[j] << " ";
	}
	cout << endl;

	BesideRoad_of_Road(521);
	for (int j = 0; j < 6; j++)
	{
		cout << BesideRoadResult[j] << " ";
	}
	cout << endl;

}

int main()
{
    std::cout << "Hello ZHH!\n"; 
	buildMap(1001);
	printMap();
//	testifRoadAccess_WhenBeside();
	findRoad(1001);
	findRoad(1002);
	findRoad(1003);
	findRoad(1004);
	findRoad(1005);
}

