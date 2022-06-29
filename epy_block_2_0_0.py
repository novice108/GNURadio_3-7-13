import numpy
from gnuradio import gr
import pmt

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class msg_block(gr.basic_block):
	def __init__(self):
		gr.basic_block.__init__(self,
			name = "Decrypt AES-256 CBC",
			in_sig = None,
			out_sig = None)
		self.message_port_register_in(pmt.intern('pdu_in'))
		self.message_port_register_out(pmt.intern('out'))
		self.set_msg_handler(pmt.intern('pdu_in'), self.handle_msg)

	def handle_msg(self, msg):
		J2 = pmt.cdr(msg)
		J3 = pmt.to_python(J2)
		s = J3.tostring()
		key_str = b"12345678123456781234567812345678" # 256bit key 12345678123456781234567812345678
		iv = b"1111222233334444"
		aesCipher = Cipher(algorithms.AES(key_str),
				modes.CBC(iv),
				backend = default_backend())
		aesEncryptor = aesCipher.encryptor()
		aesDecryptor = aesCipher.decryptor()
		plain = aesDecryptor.update(s)
		print("\n")
		print("plain : ", plain)
		print("\n")
		self.message_port_pub(pmt.intern('out'), pmt.intern(("sended encrypted message is: " + s)))
