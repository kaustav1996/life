import java.io.*;
import java.net.*;
import java.math.*;
import javax.script.ScriptEngineManager;
import javax.script.ScriptEngine;
import javax.script.ScriptException;
public class serverm {
public static void main(String[] args) throws ScriptException {
try{
	ServerSocket ss =new ServerSocket(6666);
	Socket s =ss.accept();
	DataInputStream dis =new DataInputStream(s.getInputStream());
	DataOutputStream dout= new DataOutputStream(s.getOutputStream());
	String str="";
	while(str.indexOf("exit")== -1 ){
		str =(String)dis.readUTF();
		ScriptEngineManager mgr = new ScriptEngineManager();
		ScriptEngine engine = mgr.getEngineByName("JavaScript");
		int n = new BigDecimal(engine.eval(str).toString()).intValue();
		str=Integer.toString(n);
		dout.writeUTF(str);
		dout.flush();
	}
	ss.close();
    }catch(Exception e){
	System.out.println(e);}
}
}