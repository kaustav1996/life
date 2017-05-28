import java.io.*;
import java.net.*;
public class UDPCalcServer{
	public static void main(String args[]) throws IOException {
		DatagramSocket serverSocket= new DatagramSocket(9876);
		byte[] receiveData=new byte[1024];
		byte[] sendData=new byte[1024];
		while(true){
			DatagramPacket receivePacket=new DatagramPacket(receiveData, receiveData.length);
			serverSocket.receive(receivePacket);
			String x=new String(receivePacket.getData());
			StringBuffer sentence=new StringBuffer(x.substring(0,x.indexOf(";")));
			String tempSent=sentence.toString();
			String[] temp=tempSent.split(" ");
			int ans=0;
			System.out.print(temp[0]);
			switch (temp[1].charAt(0)){
				case '+': ans=Integer.parseInt(temp[0])+Integer.parseInt(temp[2]);
							break;
				case '-': ans=Integer.parseInt(temp[0])-Integer.parseInt(temp[2]);
							break;
				case '*': ans=Integer.parseInt(temp[0])*Integer.parseInt(temp[2]);
							break;
				case 'x': ans=Integer.parseInt(temp[0])*Integer.parseInt(temp[2]);
							break;
				case '/': ans=Integer.parseInt(temp[0])/Integer.parseInt(temp[2]);
							break;
				case '%': ans=Integer.parseInt(temp[0])%Integer.parseInt(temp[2]);
							break;
			}
			String ansSent=Integer.toString(ans);
			InetAddress IPAddress = receivePacket.getAddress();
			int port=receivePacket.getPort();
			sendData=ansSent.getBytes();
			DatagramPacket sendPacket=new DatagramPacket(sendData,sendData.length,IPAddress,port);
			serverSocket.send(sendPacket);
		}
	}
}