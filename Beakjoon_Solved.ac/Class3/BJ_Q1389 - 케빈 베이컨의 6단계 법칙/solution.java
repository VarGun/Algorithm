import java.util.*;
import java.io.*;


public class solution {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        Graph g = new Graph(n);

        for(int i = 0; i < m; i++){
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st2.nextToken());
            int w = Integer.parseInt(st2.nextToken());
            g.addEdge(v-1, w-1);
        }
        for(int i = 0; i<n;i++){
            g.BFS(i);
        }
        g.setK();

        System.out.println(g.getK());

    }
}

class Graph{
    private int V;
    private LinkedList<Integer> adj[];
    private int[][] k;
    private int minIndex;
    private int minNum;
    private int maxNum;

    Graph(int v){
        V = v;
        adj = new LinkedList[v];
        k = new int[v][v+1];
        for(int i = 0; i < v; i++){
            adj[i] = new LinkedList();
        }
        maxNum = v*v;
    }

    void addEdge(int v, int w){
        adj[v].add(w);
        adj[w].add(v);
    }

    void setK(){
        for(int i = 0; i < V;i++){
            for(int j = 0; j < V; j++){
                k[i][V] += k[i][j];
            }
        }
    }
    
    int getK(){
        minNum = maxNum;
        for(int i = 0 ;i<V;i++){
            if(minNum > k[i][V]){
                minNum = k[i][V];
                minIndex = i + 1;
            }
        }
        return minIndex;
    }


    void BFS(int s){
        boolean visited[] = new boolean[V];

        LinkedList<Integer> queue = new LinkedList<>();

        visited[s] = true;
        queue.add(s);
        int s2 = s;
        

        while(queue.size() != 0){
            s = queue.poll();

            Iterator<Integer> i = adj[s].listIterator();
            while(i.hasNext()){
                int n = i.next();

                if(visited[n] == false){
                    visited[n] = true;
                    k[s2][n] = k[s2][s] + 1;
                    queue.add(n);
                }
            }

        }

    }

}
