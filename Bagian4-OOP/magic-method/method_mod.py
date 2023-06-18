# Magic method __mod__ adalah method khusus dalam Python 
# yang digunakan untuk mengatur perilaku operasi modulo (%) antara dua objek.
# method ini memungkinkan kita untuk mendefinisikan cara objek dari kelas yang kita buat berperilaku saat dioperasikan dengan operator modulo.

# Ketika operator % digunakan antara dua objek,
# Python akan mencari dan menggunakan method __mod__ untuk menentukan hasil modulo tersebut.
# method ini memungkinkan kita mengendalikan bagaimana objek dari kelas yang kita definisikan akan dikenai operasi modulo.

# Syntax:
# __mod__(self, other)
# method __mod__ dijalankan ketika operator % digunakan pada objek.
# method ini menerima dua parameter: self (objek saat ini) dan other (objek yang digunakan sebagai modulator).
# nama parameter "other" bisa diganti dengan nama apapun
