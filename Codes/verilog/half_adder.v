module main; 
  reg A,B;
  wire S,C;
  xor xor1(S,A,B);
  and and1(C,A,B);

  initial
    begin
      A=0;
      B=1;
      #5; // Wait 5 time units. 
      $display("Sum = ", S); 
      $display("Carry = ", C);
    end
endmodule
