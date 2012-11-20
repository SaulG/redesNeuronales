set key off
set term png
set output 'neurona.png'
set pointsize 0.5
set title 'Entrenamiento de la red neuronal'
set xlabel 'Iteraciones'
set ylabel 'Error'
plot 'entrenamiento.dat' using 1:2 with points pt 7 lt 1