module halfadd(S,C,A,B);
  input A, B; 
  output S, C;
  xor xor1(S, A, B);
  and and1(C, A, B); 
endmodule


module fulladd(S,Cout,Cin,A,B); 
  input Cin,A,B;
  output S,Cout; 
  wire w1,w2,w3;
  halfadd half1(w1,w2,A,B); 
  halfadd half2(S,w3,Cin,w1); 
  or or1(Cout,w3,w2);
endmodule


module main;
  reg Cin,A,B;
  wire S,Cout;
  fulladd full1(S,Cout,Cin,A,B);

  initial
      begin
        Cin=1;
        A=0;
        B=1;
        #5; // wait 5 time units
        $display("Sum = ", S);
        $display("Carry = ", Cout);
      end
endmodule