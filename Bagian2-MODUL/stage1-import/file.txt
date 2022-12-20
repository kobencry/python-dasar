Folder __pycache__ adalah folder yang dibuat oleh interpreter Python untuk menyimpan file bytecode Python yang telah dikompilasi.
File bytecode adalah versi dari source code Python yang telah dikompilasi menjadi bentuk yang lebih efisien untuk dijalankan oleh interpreter Python.
Interpreter Python akan secara otomatis mengkompilasi source code Python menjadi file bytecode saat pertama kali source code tersebut dijalankan.
Kemudian, file bytecode tersebut akan disimpan di dalam folder __pycache__ agar bisa digunakan kembali saat source code tersebut dijalankan kembali.
Dengan demikian, proses kompilasi source code tidak perlu dilakukan setiap kali source code tersebut dijalankan, sehingga program menjadi lebih cepat.

Folder __pycache__ hanya dibuat jika interpreter Python dijalankan dengan opsi -B atau -bb.
Opsi tersebut dapat diberikan ke interpreter Python melalui command line atau ditetapkan di dalam file pyproject.
toml atau tox. ini jika Anda menggunakan tool seperti Poetry atau Tox.
Jika opsi tersebut tidak diberikan, maka folder __pycache__ tidak akan dibuat.

Anda dapat menonaktifkan pembuatan folder __pycache__ dengan menggunakan opsi -B0 atau -bb0 saat menjalankan interpreter Python.
Namun, penonaktifan pembuatan folder __pycache__ dapat menyebabkan interpreter Python harus mengkompilasi source code setiap kali program dijalankan, sehingga program menjadi lebih lambat.
