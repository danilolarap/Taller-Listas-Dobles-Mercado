/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package empleado;

/**
 *Clase empleado
 * @author labinf1.pasto
 * Version 1.0
 */
private class Emplead {
    //Atributos
    private String nombre;
    private String apellido;
    private double salario;
    
    /**
     * 1=Masculino y 2=Femenino
     */
    private int sexo;
    
    /**
     * Asociaciones
     */
    
    private Fecha fechaNacimiento;
    private Fecha fechaIngresoEmpresa;
    
    /**
     * Metodos
     */
    
    /**
     * CambiarSalario
     * @param nuevoSalario nuevo sueldo ingresado por el usuario
     * Cambia el sueldo del empleado
     */
    public void CambiarSalario(double nuevoSalario){
        //Aqui va el codigo
        this.salario=nuevoSalario;
    }
    
    /**
     * DarSalario
     * @return Salario
     * Retorna el salario del empleado
     */
    public double DarSalario(){
        //Aqui va el codigo
        return this.salario;
    }
    
    /**
     * CalculoPrestaciones
     * @return Prestaciones
     * Calculo de las prestaciones en base a su salario y fehca de ingreso
     */
    public double CalculoPrestaciones(){
        //Aqui va el codigo
    }
    
   /**
    * Aumentarsalario
    * @param aumento Bonificacion al salario digitado por el usuario
    * @return nuevoSalario
    * Metodo que permite agregar bonificacion al salario del empleado
    */
    public double Aumentarsalario(double aumento){
        //Aqui va el codigo
        this.salario=this.salario+aumento;
        return this.salario;
    }
    
    /**
     * DuplicarSalario
     * Metodo que permite duplicar el salario del empleado
     */
    public void DuplicarSalario(){
        //Aqui va el codigo
        this.salario=this.salario * 2;
    } 
    
    /**
     * CalcularSalarioAnual
     * Metodo que permite ver el salario anual del empleado
     */
    public double CalcularSalarioAnual(){
        //Aqui va el codigo 
        double SalarioAnual=this.salario * 12;
        return SalarioAnual;
    }
    
    /**
     * CalcularImpuestoAnual
     * @return Impuesto Anual
     * Metodo que calcula el impuesto anual del empleado
     */
    public double CalcularImpuestoAnual(){
        //Aqui va el codigo
        return this.CalcularSalarioAnual()* 0.19;
    }
    
}
