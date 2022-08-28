import java.util.Arrays;
import java.util.Scanner;

//실수 내용: 0일때 최소거리의 총합 1을 기록하고 바로 빠져나오도록 설계
public class Solution {
    static int MIN = Integer.MAX_VALUE;
    static int N;
    
    //visit: 낚시 아재들 체크, //arr: 관련 정보 저장, // check: 낚시터 순서
    static void dfs(int depth, int[] visit, int[][] arr, boolean[] check, int sum) {
        //System.out.println("depth: " + depth + " check: " + Arrays.toString(check));
        if(depth == 3) {
            //System.out.println("depth: " + depth + " sum: " + sum);
            MIN = Math.min(sum, MIN);
            //System.out.println("MIN: " + MIN);
            return;
        }
        
        for(int i=0; i<3; i++) {
            //System.out.println(i + " check : "+Arrays.toString(check));
            //System.out.println("depth: " + depth + " i : " + i + " check: " + Arrays.toString(check));
            if(!check[i]) {
                check[i] = true;
                
                int[] result = fill(i, visit, arr[i][0], arr[i][1]);
                //System.out.println(Arrays.toString(result));
                
                if(result[0] == 0) { //하나만 최적의 해일 때
                    dfs(depth+1, visit, arr, check, sum + result[2]);
                }else { // 두개가 최적의 해일 때
                    //System.out.println("들어오나");
                    int[] visit2 = new int[N];
                    for(int j=0; j<N; j++) {
                        visit2[j] = visit[j];
                    }
                    //System.out.println("들어오나");
                    visit2[arr[i][0]-result[1]] = -1;
                    visit2[arr[i][0]+result[1]] = i;
                    //System.out.println("VISIT2 : " + Arrays.toString(visit2));
                    dfs(depth+1, visit2, arr, check, sum + result[2]);
                    dfs(depth+1, visit, arr, check, sum + result[2]);
                }
                
                check[i] = false;
                remove(i, visit); //visit에서 해당하는 숫자들 삭제
            }
        }
    }
    
    static int[] fill(int number, int[] visit, int center, int people) {
        int p = people; //배치할 사람의 수
        int gap = 0;
        int sum = 0;
        int res = 0; //0이면 한개의 해, 1이면 2개의 해
        //0일 때는 오른쪽 왼쪽 겹치므로 따로 분리
        if(visit[center] == -1) {
            visit[center] = number;
            p--;
            sum += 1;
        }
        
        if(p==0) {
            return new int[] {res, gap, sum};
        }
        
        for(int g=1; g<N; g++) {
            int left = center - g;
            int right = center + g;
            boolean flag1 = false; //flag가 한 번이라도 켜지면 반복문 지속
            boolean flag2 = false;
            
            if(left >= 0) {
                flag1 = true;
                
                if(visit[left]==-1 && p>0) { //만약 빈칸이라면
                    visit[left] = number;
                    p--;
                    sum += g+1;
                }
            }
            
            
            if(right < N) {
                flag2 = true;
                
                if(visit[right]==-1 && p>0) { //만약 빈칸이라면
                    visit[right] = number;
                    p--;
                    sum += g+1;
                }else if(flag1 && visit[right]==-1 && p==0) { //똑같은 기회인데 p가 부족한 경우라면
                    res = 1;
                    gap = g;
                }
            }
            
            if((!flag1 && !flag2) || p == 0) { //반복문 종료
                g = N;
            }
        }
        
        return new int[] {res, gap, sum};
    }
    
    static void remove(int number, int[] visit) {
        //값을 다시 빈자리로 초기화
        for(int i=0; i<N; i++) {
            if(visit[i] == number) {
                visit[i] = -1;
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int t=1; t<T+1; t++) {
            MIN = Integer.MAX_VALUE;
            N = sc.nextInt();
            int[] visit = new int[N];
            Arrays.fill(visit, -1);//방문 안한 곳은 -1 표시
            
            int[][] arr = new int[3][2];
            for(int n=0; n<3; n++) {
                arr[n][0] = sc.nextInt()-1;
                arr[n][1] = sc.nextInt();
            }
            
            dfs(0, visit, arr, new boolean[3], 0);
            
            System.out.println("#"+t+" "+MIN);
        }
    }

}