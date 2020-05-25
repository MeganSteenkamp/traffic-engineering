Minimize 
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

	capD11: x111 + x211 + x311 - d11 <= 0
	capD21: x121 + x221 + x321 - d21 <= 0
	capD12: x112 + x212 + x312 - d12 <= 0
	capD22: x122 + x222 + x322 - d22 <= 0
	capD13: x113 + x213 + x313 - d13 <= 0
	capD23: x123 + x223 + x323 - d23 <= 0

	transit1: x111 + x112 + x113 + x211 + x212 + x213 + x311 + x312 + x313 - r <= 0
	transit2: x121 + x122 + x123 + x221 + x222 + x223 + x321 + x322 + x323 - r <= 0

	bin11: u111 + u121 = 2
	bin12: u112 + u122 = 2
	bin13: u113 + u123 = 2
	bin21: u211 + u221 = 2
	bin22: u212 + u222 = 2
	bin23: u213 + u223 = 2
	bin31: u311 + u321 = 2
	bin32: u312 + u322 = 2
	bin33: u313 + u323 = 2

	eqlPath111: 2 x111 - 2 u111 = 0
	eqlPath121: 2 x121 - 2 u121 = 0
	eqlPath112: 2 x112 - 3 u112 = 0
	eqlPath122: 2 x122 - 3 u122 = 0
	eqlPath113: 2 x113 - 4 u113 = 0
	eqlPath123: 2 x123 - 4 u123 = 0
	eqlPath211: 2 x211 - 3 u211 = 0
	eqlPath221: 2 x221 - 3 u221 = 0
	eqlPath212: 2 x212 - 4 u212 = 0
	eqlPath222: 2 x222 - 4 u222 = 0
	eqlPath213: 2 x213 - 5 u213 = 0
	eqlPath223: 2 x223 - 5 u223 = 0
	eqlPath311: 2 x311 - 4 u311 = 0
	eqlPath321: 2 x321 - 4 u321 = 0
	eqlPath312: 2 x312 - 5 u312 = 0
	eqlPath322: 2 x322 - 5 u322 = 0
	eqlPath313: 2 x313 - 6 u313 = 0
	eqlPath323: 2 x323 - 6 u323 = 0


Bounds
	r >= 0
	x213 >= 0
	x111 >= 0
	x223 >= 0
	x222 >= 0
	x122 >= 0
	x212 >= 0
	x123 >= 0
	x313 >= 0
	x112 >= 0
	x221 >= 0
	x312 >= 0
	x322 >= 0
	x321 >= 0
	x323 >= 0
	x121 >= 0
	x211 >= 0
	x311 >= 0
	x113 >= 0
	c22 >= 0
	c32 >= 0
	c31 >= 0
	c12 >= 0
	c11 >= 0
	c21 >= 0
	d22 >= 0
	d23 >= 0
	d13 >= 0
	d12 >= 0
	d11 >= 0
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