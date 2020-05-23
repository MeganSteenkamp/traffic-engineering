Minimise: 
	obj: r

Subject To
	dem11: x111 + x121 = 2
	dem12: x112 + x122 = 3
	dem13: x113 + x123 = 4
	dem21: x211 + x221 = 3
	dem22: x212 + x222 = 4
	dem23: x213 + x223 = 5
	dem31: x311 + x321 = 4
	dem32: x312 + x322 = 5
	dem33: x313 + x323 = 6
	capS11: x111 + x112 + x113 - c11 <= 0
	capS12: x121 + x122 + x123 - c12 <= 0
	capS21: x211 + x212 + x213 - c21 <= 0
	capS22: x221 + x222 + x223 - c22 <= 0
	capS31: x311 + x312 + x313 - c31 <= 0
	capS32: x321 + x322 + x323 - c32 <= 0
	transit1: x111 + x112 + x113 + x211 + x212 + x213 + x311 + x312 + x313 - r <= 0
	transit2: x121 + x122 + x123 + x221 + x222 + x223 + x321 + x322 + x323 - r <= 0
	bin11: u_111 + u_121 = 2
	bin12: u_112 + u_122 = 2
	bin13: u_113 + u_123 = 2
	bin21: u_211 + u_221 = 2
	bin22: u_212 + u_222 = 2
	bin23: u_213 + u_223 = 2
	bin31: u_311 + u_321 = 2
	bin32: u_312 + u_322 = 2
	bin33: u_313 + u_323 = 2	eqlPath111: x111 = (u111 * 2) / 2
	eqlPath121: x121 = (u121 * 2) / 2
	eqlPath112: x112 = (u112 * 3) / 2
	eqlPath122: x122 = (u122 * 3) / 2
	eqlPath113: x113 = (u113 * 4) / 2
	eqlPath123: x123 = (u123 * 4) / 2
	eqlPath211: x211 = (u211 * 3) / 2
	eqlPath221: x221 = (u221 * 3) / 2
	eqlPath212: x212 = (u212 * 4) / 2
	eqlPath222: x222 = (u222 * 4) / 2
	eqlPath213: x213 = (u213 * 5) / 2
	eqlPath223: x223 = (u223 * 5) / 2
	eqlPath311: x311 = (u311 * 4) / 2
	eqlPath321: x321 = (u321 * 4) / 2
	eqlPath312: x312 = (u312 * 5) / 2
	eqlPath322: x322 = (u322 * 5) / 2
	eqlPath313: x313 = (u313 * 6) / 2
	eqlPath323: x323 = (u323 * 6) / 2

Bounds
	r >= 0
	x321 >= 0
	x322 >= 0
	x112 >= 0
	x113 >= 0
	x123 >= 0
	x121 >= 0
	x223 >= 0
	x312 >= 0
	x323 >= 0
	x211 >= 0
	x213 >= 0
	x221 >= 0
	x311 >= 0
	x111 >= 0
	x222 >= 0
	x313 >= 0
	x212 >= 0
	x122 >= 0
	c12 >= 0
	c31 >= 0
	c21 >= 0
	c32 >= 0
	c11 >= 0
	c22 >= 0
	d13 >= 0
	d11 >= 0
	d23 >= 0
	d12 >= 0
	d22 >= 0
	d21 >= 0

Binaries
	u111
	u121
	u112
	u122
	u113
	u123
	u211
	u221
	u212
	u222
	u213
	u223
	u311
	u321
	u312
	u322
	u313
	u323

End