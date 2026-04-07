/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package simuladorbancario;

/**
 *
 * @author labinf1.pasto
 */
public class SimuladorBancari {
    //Atributos
    private String nombre;
    private String cedula;
    
    /**
     * Asociaciones
     */
    
    private CuentaAhorros cuentaAhorros;
    private CDT CDT;
    
    private CuentaCorriente cuentaCorriente;
    //Atributos
    private double saldo;
    
    /**
     * Metodos
     */
    
    /**
     * ConsignarValor
     * @param valor
     * @return saldo
     * Metodo que permite consignar un monto a la cuenta
     */
    public double ConsignarValor(double valor){
        //Aqui va el codigo
        this.saldo=this.saldo+valor;
        return this.saldo;
        
    }
    
    public double DarSaldo(){
        //Aqui va el codigo
    }
    
    public double RetirarValor(double valor){
        //Aqui va el codigo
        this.saldo=this.saldo-valor;
        return this.saldo;
    }
    
    public double DarInteresMensual(){
        //Aqui va el codigo
        
    }
    
    public double SaldoTotal 
}
