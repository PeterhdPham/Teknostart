//MOTOR SETUP
const int E1 = 3; ///<Motor1 Speed - Front Right
const int E2 = 11;///<Motor2 Speed - Front Left
const int E3 = 5; ///<Motor3 Speed - Back Right
const int E4 = 6; ///<Motor4 Speed - Back Left

const int M1 = 7; ///<Motor1 Direction - Front Right
const int M2 = 8;///<Motor2 Direction - Front Left
const int M3 = 12; ///<Motor3 Direction - Back Right
const int M4 = 4; ///<Motor4 Direction - Back Left

/////////LOGIC/////////////////////////////////
//INPUT PINS
int drive = A0;
int reverse = A1;
int leftTurn = A2;
int rightTurn = A3;

//BOOLS
int go = 0;
int back = 0;
int left = 0;
int right = 0;


//SPEEDS
int drivingSpeed = 150;
int turningSpeed = 50;

enum Motor {
  MotorRight,
  MotorLeft,
  MotorBoth
};

//////DRIVING FUNCTIONS//////////////////////
void speedSet(Motor motor, int Speed) {
    if(motor == MotorRight){
        analogWrite(E1, Speed);
        analogWrite(E3, Speed);
    }
    else if(motor == MotorLeft){
        analogWrite(E2, Speed);
        analogWrite(E4, Speed);
    }
    else if(motor == MotorBoth){
        analogWrite(E1, Speed);
        analogWrite(E2, Speed);
        analogWrite(E3, Speed);
        analogWrite(E4, Speed);
    }
}

//DRIVING FUNCTION
void driving(Motor motor, bool Direction) {
    if (motor == MotorBoth){
        Direction = !Direction;
        digitalWrite(M1, Direction);
        digitalWrite(M2, Direction);
        digitalWrite(M3, Direction);
        digitalWrite(M4, Direction);
    }
    else if (motor == MotorRight){
        digitalWrite(M1, Direction);
        digitalWrite(M3, Direction);
    }
    else if (motor == MotorLeft){
        digitalWrite(M2, Direction);
        digitalWrite(M4, Direction);
    }
}



////SETUP///////////////////////
void setup() {
  Serial.begin(9600);   
  Serial.println("Starting session...");

  //SET PINS 
  pinMode(drive, INPUT_PULLUP);
  pinMode(reverse, INPUT_PULLUP);
  pinMode(leftTurn, INPUT_PULLUP);
  pinMode(rightTurn, INPUT_PULLUP);

  for(int i=3;i<=8;i++) {
      pinMode(i,OUTPUT);
      digitalWrite(i, LOW);  // Initiate as LOW
  }

  for(int i=11;i<=13;i++) {
      pinMode(i,OUTPUT);
      digitalWrite(i, LOW);  // Initiate as LOW
  }
}


void loop() {
//UPDATING THE BOOLEANS
go = digitalRead(drive);
back = digitalRead(reverse);
left = digitalRead(leftTurn);
right = digitalRead(rightTurn);


/////FORWARD DRIVE/////////////////////////////////////////
if (go && !back) {  
    driving(MotorBoth, 0);  
    if (right) {
        speedSet(MotorRight, turningSpeed);
    } else if (left) {
        speedSet(MotorLeft, turningSpeed);
    } else {
        speedSet(MotorBoth, drivingSpeed);
    }
}


//REVERSE
else if(back && !go){
    driving(MotorBoth, 1);
    //REVERSE WITH RIGHTTURN
    if(right){
    speedSet(MotorRight,turningSpeed);
    }
    //REVERSE WITH LEFTTURN
    else if(left){
    speedSet(MotorLeft, turningSpeed);
    }
    else{
    speedSet(MotorBoth, drivingSpeed);      
    Serial.println("REVERSE");
    }
}



//RIGHTTURN
else if(right && !go && !back){
    speedSet(MotorBoth, turningSpeed);
    if(!left){
    digitalWrite(M1,1);
    digitalWrite(M3,1);
    digitalWrite(M2,0);
    digitalWrite(M4,0);
    Serial.println("RIGHTTURN");
    }
    
    //IF YOU PRESS BOTH LEFT AND RIGHT
    else{
    driving(MotorBoth, 0);
    }
}

//LEFTTURN
else if(left && !go && !back){
    speedSet(MotorBoth, turningSpeed);
    if(!right){
    digitalWrite(M1,0);
    digitalWrite(M3,0);
    digitalWrite(M2,1);
    digitalWrite(M4,1);
    Serial.println("LEFTTURN");
    }

//IF YOU PRESS BOTH LEFT AND RIGHT
    else{
    driving(MotorBoth, 0);
    }
}

//IF YOU DON'T PRESS ANYTHNIG
else{
    speedSet(MotorBoth, 0);
    Serial.println("STOP");
}
}
