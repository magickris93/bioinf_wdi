#!/bin/bash
# -*- coding: utf-8 -*-

import re

# Zadanie 5

def tramwaje(tekst):
	reg_exp_sen = r'([A-Z][^.]*.)'
	sentences = []
	sentences = re.findall(reg_exp_sen, tekst)

	r_dict = {	'tramwaj' : r'\b(\d\d?)\b',
				'specjalny' : r'\b[A-Z]\b',
				'autobus' : r'\b[1-4]\d\d\b',
				'pospieszny' : r'\b50[1-9]|[5-9]\d\d\b',
				'ekspresowy' : r'\bE-\d\b',
				'nocny' : r'\bN(\d{2})\b'}

	for s in sentences :
		found = {}
		for reg in r_dict:
			found[reg] = re.findall(r_dict[reg], s)
		count = 0
		for k in found:
			if len(found[k]) != 0:
				print len(found[k]), 'x', str(k)+',',
				count += 1
		if count >= 3:
			print '!',
		print
