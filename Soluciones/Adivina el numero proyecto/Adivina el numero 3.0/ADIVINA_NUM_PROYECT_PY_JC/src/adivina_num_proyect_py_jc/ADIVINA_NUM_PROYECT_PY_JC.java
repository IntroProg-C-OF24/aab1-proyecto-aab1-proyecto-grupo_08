package adivina_num_proyect_py_jc;
import java.util.Scanner;
public class ADIVINA_NUM_PROYECT_PY_JC {
    public static void main(String[] args) {
        int nIng, nAdiv, intentos, limMay,limMen,maxintentos;
        String pistas,rango,rules;
        boolean adivino=false;
        Scanner put=new Scanner(System.in);
        System.out.println("---------------------");
        System.out.println("CONFIGURE SU PARTIDA");
        System.out.println("---------------------");
        System.out.println("-Si desea la configuracion por defecto escriba (CPU)");
        System.out.println("-Si desea configurar manualmente su partida escriba (YO)");
        rules = put.next(); //SI EL JUGADOR ELIGE CPU SE AUTOESTABLECEN LAS REGLAS, SI ELIGE YO, LAS ELIGE ESTE MISMO
        if(rules.equals("CPU")){
            intentos=10;
            pistas="SI";
            nAdiv = (int)(Math.random()*(100-1+1)+1);
            rango="1 - 100";
        }
        else{ 
            System.out.println("1-INTENTOS");
            System.out.println("INGRESE EL NUMERO DE INTENTOS: ");
            intentos=put.nextInt();
            System.out.println("2-PISTAS");
            System.out.println("-Si quiere recibir pistas sobre el numero secreto escriba (SI)");
            System.out.println("-Si no quiere recibir pistas escriba (NO)");
            pistas = put.next();   //SI RESPONDE "SI" SE LE AVISARA AL JUGADOR SI EL NUMERO INGRESADO ES MAYOR O MENOR AL NUMERO SECRETO        
            System.out.println("3-RANGO");
            System.out.println("INGRESE EL LIMITE MAYOR: ");
            limMay = put.nextInt();
            System.out.println("INGRESE EL LIMITE MENOR: ");
            limMen= put.nextInt();
            nAdiv = (int)(Math.random()*(limMay-limMen+1)+limMen);
            rango=limMen+" - "+limMay;
        }
        maxintentos = intentos;
        System.out.println("--------------------------------------------------");
        System.out.println("INICIO DE LA PARTIDA");
        System.out.println("INTENTOS: "+intentos+"  -  PISTAS: "+pistas+"  -  RANGO: "+rango);
        System.out.println("--------------------------------------------------");
        if (pistas.equals("SI"))    //SI SE ACEPTARON LAS PISTAS, EL JUEGO COMIENZA CON UNA PISTA INICIAL
            if(nAdiv%2==0)
                System.out.println("TEN EN CUENTA QUE EL NUMERO ES PAR");
            else
                System.out.println("TEN EN CUENTA QUE EL NUMERO ES IMPAR");
                
        System.out.println("INGRESE UN NUMERO "+rango);
        while(intentos>=1){
            nIng = put.nextInt();
            intentos--;
            if(nIng==nAdiv){
                adivino=true;
                break;
            }
            else if(intentos>=1&&(pistas.equals("SI")))
                    if(nAdiv>nIng)
                        System.out.println("INTENTA CON UNO MAYOR");
                    else
                        System.out.println("INTENTA CON UNO MENOR");
            
            System.out.println("TE QUEDAN: "+intentos+" intentos");
        }
        if(adivino)
            System.out.println("GANASTE, LO LOGRASTE EN: "+(maxintentos-intentos)+" INTENTOS");
        else
            System.out.println("PERDISTE");
    }     
}