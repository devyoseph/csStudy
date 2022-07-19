import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	static int[][][] map;
	static int N;
	static boolean possible;
	
	//9칸의 좌표
	static int[] dx = {-1,-1,-1, 0, 0,0, 1,1,1};
	static int[] dy = { 1, 0,-1, 1,-1,0, 1,0,-1};
	
	//기둥에 대한 검사
	static boolean gidung(int x, int y) {
		//System.out.println("기둥검사");
		//바닥 위에 있으면 무조건 true || 아래에 기둥이 있어도 true
		if( y==0 || (y>0 && map[x][y-1][0] == 1)) {
			return true;
		}
		
		//보의 한쪽 끝 부분 위에 있거나
		
		//1) 끝점에 있을 때
		if( (x==0 && map[x][y][1] == 1) || (x==N && map[x-1][y][1] == 1)) return true;
		
		//2) 보 위에 있을 때
		if( x>0 && x<N && (map[x-1][y][1] == 1 || map[x][y][1] == 1)) {
			//int cnt = 0;
			
			//기둥 양쪽으로 붙어있는 보를 세어준다.
			//아니 이 조건 떄문에 계속....[[ 연속된 보 위에서도 기둥을 세울 수 있다. ]]
			return true;
		}
		
		return false;
	}
	
	//보에 대한 검사
	//한쪽 끝 부분이 기둥 위에 있거나 또는 양쪽 끝 부분이 다른 보와 동시 연결
	static boolean bo(int x, int y) {
		//그냥 끝점: 예외처리 때문에 넣어줌
		if(x==N) return true;
		
		//양쪽 모두 보
		if(x > 0 && x < N-1 && map[x-1][y][1] == 1 && map[x+1][y][1] == 1) {
			return true;
		}
		
		//보는 무조건 바닥으로 주어지지 않는다.
		//양쪽 끝 중 하나라도 기둥 ON
		if(map[x][y-1][0] == 1 || map[x+1][y-1][0] == 1) {
			return true;
		}
		
		return false;
	}
	
	static int[][] solution(int n, int[][] build_frame){
		N = n;
		map = new int[n+1][n+1][2];
		
		for(int[] bf : build_frame) {
			int x = bf[0]; //열
			int y = bf[1]; //행
			int a = bf[2]; //기둥(0), 보(1)
			int b = bf[3]; //삭제(0), 설치(1)
			
			if(b==1) { //설치시: 가능한지 메서드로 확인
				if(a == 0 && gidung(x, y)) {
					//System.out.println("기둥: "+x+" "+y);
					map[x][y][0] = 1;
				}else if(a == 1 && bo(x, y)) {
					//System.out.println("보: "+x+" "+y);
					map[x][y][1] = 1;
				}
			}else { //삭제시: 가능한지 dfs 등으로 확인
				possible = true;
				map[x][y][a] = 0; //조형물을 지워보기
				//굳이 쓸 필요없었다
				for(int i=0; i<9; i++) {
					int row = x + dx[i];
					int col = y + dy[i];
					if(row < 0 || row > N || col < 0 || col >N) continue;
					
					for(int j=0; j<2; j++) {
						if(map[row][col][j] == 1) {
							if(j==0 && !gidung(row, col)) { //설치가 더이상 불가능하면
								possible = false;
							}else if(j==1 && !bo(row, col)) {
								possible = false;
							}
						}
						
						if(!possible) {
							j = 2;
							i = 9;
						}
					}
				}
				
				if(!possible) map[x][y][a] = 1; //불가능하면 원상태 복구
			}
		}
		int count = 0;
		for(int k=0; k<2; k++) {
			//System.out.println("==============");
			for(int i=0; i<=N; i++) {
				for(int j=0; j<=N; j++) {
					count += map[i][j][k];
					//System.out.print(map[i][j][k]);
				}
				//System.out.println();
			}
		}
		//System.out.println(count);
		int[][] answer = new int[count][3];
		count = 0;
		for(int i=0; i<=N; i++) {
			for(int j=0; j<=N; j++) {
				for(int k=0; k<2; k++) {
					if(map[i][j][k] == 1) {
						answer[count++] = new int[] {i,j,k};
					}
				}
			}
		}
		for(int[] a: answer) {
			System.out.println(Arrays.toString(a));
		}
        return answer;
	}
	public static void main(String[] args) throws IOException {
		int[][] a = {{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
		solution(5, a);
		System.out.println(" ");
		int[][] b = {{0,0,0,1},{2,0,0,1},{4,0,0,1},{0,1,1,1},{1,1,1,1},{2,1,1,1},{3,1,1,1},{2,0,0,0},{1,1,1,0},{2,2,0,1}};
		solution(5, b);
		int[][] c =  {{2, 0, 0, 1}, {100, 0, 0, 1}, {100, 1, 1, 1}, {99, 1, 1, 1}, {99, 1, 0, 1}, {99, 0, 0, 1}};
		solution(100, c);
	}
}
