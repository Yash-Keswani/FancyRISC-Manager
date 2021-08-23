class LU:
	def add(params):
		"adds two integers"
		return {
			'main': params[0] + params[1],
			'flags': f"{int(params[0] + params[1] > 255)}000"
		}

	def sub(params):
		"subtracts two integers"
		return {
			'main': params[0] - params[1],
			'flags': f"{int(params[0]-params[1] > 255)}001"
		}
	
	def movi(params):
		"Move Immediate"
		return {
			'main': params[0] + params[1],
			'flags': f"{int(params[0] + params[1] > 255)}010"
		}

	def movr(params):
		"Move Register"
		return {
			'main': params[0] - params[1],
			'flags': f"{int(params[0] + params[1] > 255)}011"
		}
	
	def ld(params):
		"Loads data"
		return {
			'main': params[0] + params[1],
			'flags': f"{int(params[0] + params[1] > 255)}100"
		}

	def st(params):
		"Store"
		return {
			'main': params[0] - params[1],
			'flags': f"{int(params[0] + params[1] > 255)}101"
		}
	def mul(params):
		"multiplies two integers"
		return {
			'main': params[0] * params[1],
			'flags': f"{int(params[0] * params[1])}110"
		}

	def div(params):
		"divides two integers"
		return {
			'main': params[0]/params[1],
			'flags': f"{int(params[0] / params[1] > 255)}111"
		}
	def rs(params):
		"RIGHT SHIFT"
		return {
			'main': params[0] + params[1],
			'flags': f"{int(params[0] + params[1] > 255)}1000"
		}

	def ls(params):
		"LEFT SHIFT"
		return {
			'main': params[0] - params[1],
			'flags': f"{int(params[0] + params[1] > 255)}1001"
		}
	def hlt(params):
		"stops running code"
		return {}
	

	switcher = {
		0b00000: add,
		0b00001: sub,
		0b00010: movi,
		0b00011: movr,
		0b00100: ld,
		0b00101: st,
		0b00110: mul,
		0b00111: div,
		0b01000: rs,
		0b01001: ls,
		0b01010: xor,
		0b01011: or,
		0b01100: and,
		0b01101: not,
		0b01110: cmp,
		0b01111: jmp,
		0b10000: jlt,
		0b10001: jgt,
		0b10010: je,
		0b10011: hlt,
	}

	@classmethod
	def call(cls, opc: int, params: list) -> dict:
		"""
		calls the function for the given opcode and parameters.

		all parameters are integers in raw form.

		note the purposes of the three output values:
			- main value will contain the main output, which will be stored in a registry.
			- alter value will contain either a second output value [only for div instruction].
			- branch value will contain whether or not to follow branch instruction.
			- flags value will contain the new value of the last 4 bits in the FLAGS register.

		it is to be noted that the alter, branch, and flags values can be merged into one; but they are kept separate for clearer documentation.
		"""
		return {
			'main'  : cls.switcher[opc](params)['main'],
			'alter' : cls.switcher[opc](params)['alter'] or 0,
			'branch': cls.switcher[opc](params)['branch'] or 0,
			'flags' : cls.switcher[opc](params)['flags'] or '0000'
		}
