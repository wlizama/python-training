import threading, zipfile

class AsyncZip(threading.Thread):
  
  def __init__(self, arch_ent, arch_sal):
    threading.Thread.__init__(self)
    self.arch_ent = arch_ent
    self.arch_sal = arch_sal
 
  def run(self):
    f = zipfile.ZipFile(self.arch_sal, 'w', zipfile.ZIP_DEFLATED)
    f.write(self.arch_ent)
    f.close()
    print('Terminó zip en segundo plano de: ', self.arch_ent)


seg_plano = AsyncZip('large_lorem.txt', 'miarchivo.zip')
seg_plano.start()
print('El programa principal continúa la ejecución en primer plano.')
seg_plano.join() # esperar que termine la tarea en segundo plano
print('El programa principal esperó hasta que el segundo plano terminara.')