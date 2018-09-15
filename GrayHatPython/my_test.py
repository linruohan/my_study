import  my_debugger
debugger=my_debugger.debugger()

# debugger.load("C:\\Windows\\SysWOW64\\calc.exe")

pid=input("Enter the PID of the process to attach to:")
debugger.attach(int(pid))
debugger.run()
debugger.detach()

# threadList=debugger.enumerate_threads()
# print(threadList)
# #对于列表中的每一个线程，我们试图提取相应的上下文信息
# for thread in threadList:
#     thread_context=debugger.get_thread_context(thread)
#     #输出寄存器信息
#     #%08x就是8位的十六进制，不够加0补充
#     print("[*] Dumping registers for thread ID:0x%08x" % thread)
#     print("[**] EIP:0x%08x" % thread_context.Eip)
#     print("[**] ESP:0x%08x" % thread_context.Esp)
#     print("[**] EBP:0x%08x" % thread_context.Ebp)
#     print("[**] EAX:0x%08x" % thread_context.Eax)
#     print("[**] EBX:0x%08x" % thread_context.Ebx)
#     print("[**] ECX:0x%08x" % thread_context.Ecx)
#     print("[**] EDX:0x%08x" % thread_context.Edx)
#     print("[*] END DUMP")
#
# debugger.detach()
