
class Calculator{
    constructor(previousOperandandTextElement,currentOperandandTextElement){
        this.previousOperandandTextElement= previousOperandandTextElement
        this.currentOperandandTextElement= currentOperandandTextElement
        this.clear()
    }
 clearAll(){

    this.previousOperand = '';
    this.currentOperand= '';
    this.operation= '';

 }

    clear(){
    this.previousOperand = ''
    this.currentOperand= ''
    this.operation= undefined
    
    
    }
    
    deletes() {
       
       this.currentOperand = this.currentOperand.toString().slice(0, -1)
     /*  if(this.operation!=null){
        this.operation = this.operation.toString().slice(0, -1)
        this.previousOperand = this.previousOperand.toString().slice(0, -1)
        }
       */ 

    }
  
    appendNumber(number) {
      if(number==='.' && this.currentOperand.includes('.')) return
      this.currentOperand=this.currentOperand.toString() + number.toString()
    }
  
    chooseOperation(operation) {
        if(this.currentOperand==='')return
        if(this.previousOperand!==''){
            this.compute()
        }
          this.operation=operation
          this.previousOperand= this.currentOperand
          this.currentOperand=''
    }

    compute() {

        let computation
        const prev = parseFloat(this.previousOperand)
        const current=parseFloat(this.currentOperand)
        if(isNaN(prev)|| isNaN(current))return
        switch(this.operation){
            case '+':
                computation = prev + current
                console.log(computation)
                break
            case '-':
                 computation = prev - current
                break  
            case '*':
                computation = prev * current
                break
            case '÷':
                computation = prev / current
                break 
            default:     
                return
        }
        this.currentOperand=computation
        this.operation=undefined
        this.previousOperand=''

    }
   
    getDisplayNumber(){
       return number
    }



    updateDisplay() {
        this.currentOperandandTextElement.innerText=
        this.currentOperand
        if(this.operation!=null){
         this.previousOperandandTextElement.innerText=
         `${this.previousOperand} ${this.operation}`    
        }
 
    }



}



const numberButtons = document.querySelectorAll('[data-number]')
const operationButtons = document.querySelectorAll('[data-operation]')
const equalsButton= document.querySelector('[data-equals]')
const deleteButton= document.querySelector('[data-delete]')
const allClearsButton= document.querySelector('[data-all-clear]')
const previousOperandandTextElement=
 document.querySelector('[data-previous-operand]')
const currentOperandandTextElement= 
document.querySelector('[data-current-operand]')



const calculator= new Calculator(previousOperandandTextElement,currentOperandandTextElement)

numberButtons.forEach(button =>{
  button.addEventListener('click', () =>{
    calculator.appendNumber(button.innerText)
    calculator.updateDisplay()
})
})

operationButtons.forEach(button =>{
    button.addEventListener('click', () =>{
      calculator.chooseOperation(button.innerText)
      calculator.updateDisplay()
  })
  })

equalsButton.addEventListener('click', button =>{
    calculator.compute()
    calculator.updateDisplay()
})

allClearsButton.addEventListener('click', button =>{
    calculator.clearAll()
    calculator.updateDisplay()
})

deleteButton.addEventListener('click', button =>{
    calculator.deletes()
    calculator.updateDisplay()
})

const checkbox=document.getElementById('checkbox');
checkbox.addEventListener('change', ()=>{
 document.body.classList.toggle('green-mode');
});