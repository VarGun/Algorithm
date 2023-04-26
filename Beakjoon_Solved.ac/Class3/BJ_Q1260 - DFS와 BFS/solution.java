import java.util.*;

public class solution {
    public static void main(String[] args) {
        
    }
}
class Graph{
    private int V;
    private LinkedList<Integer> adj[];
    private ArrayList<Integer> dfsList;
    private ArrayList<Integer> bfsList;

    void Graph(int v){
        V = v;
        for(int i = 0; i<v; i++){
            adj = new LinkedList[v];
        }

        dfsList = new ArrayList<>();
        bfsList = new ArrayList<>();
    }

    void addEdge(int v, int w){ // 삽입과 동시에 정렬 , 최대값 정해놓고 그거보다 크면 add / 아니면 iterator 사용
        Iterator<Integer> adj_v = adj[v].listIterator();
        Iterator<Integer> adj_w = adj[w].listIterator();
        if(adj[v].size() == 0){
            adj[v].add(w);
        }
        else{

        }
        adj[w].add(v);
    }

    void BFS(int s){
        
        boolean[] visited = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(s);
        visited[s] = true;
        
        while(queue.size() != 0){
            s = queue.poll();

            bfsList.add(s);

            Iterator<Integer> i = adj[s].listIterator();

            while(i.hasNext()){
                int n = i.next();

                if(visited[n] == false){
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
    
    void DFS(int s){

    }



}