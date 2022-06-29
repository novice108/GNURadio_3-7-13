import numpy
from gnuradio import gr
import pmt

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

textboxValue = ""

class msg_block(gr.basic_block):
	def __init__(self):
		gr.basic_block.__init__(self,
			name = "Encrypt AES-256 CBC",
			in_sig = None,
			out_sig = None)
		self.message_port_register_in(pmt.intern('msg_in'))
		self.message_port_register_out(pmt.intern('out'))
		self.set_msg_handler(pmt.intern('msg_in'), self.handle_msg)
		os.system('clear')

	def handle_msg(self, msg):
		os.system('clear')		
		global textboxValue
		textboxValue = pmt.write_string(msg)
		_len = len(textboxValue)
		if len(textboxValue) < 32:
			padding_size = 32
			textboxValue = textboxValue.ljust(padding_size)
		else:
			textboxValue = textboxValue[0:32]
		
		_len = len(textboxValue) # get length of string
		key_str = b"12345678123456781234567812345678" # 256bit key
		iv = b"1111222233334444"
		aesCipher = Cipher(algorithms.AES(key_str),
				modes.CBC(iv),
				backend = default_backend())
		aesEncryptor = aesCipher.encryptor()
		aesDecryptor = aesCipher.decryptor()
		ciphertext = aesEncryptor.update(textboxValue)
		textboxValue = ciphertext
		a = numpy.array([ord(c) for c in textboxValue])		
		self.message_port_pub(pmt.intern('out'), pmt.cons(pmt.make_dict(), pmt.pmt_to_python.numpy_to_uvector(numpy.array(a, numpy.uint8))))
