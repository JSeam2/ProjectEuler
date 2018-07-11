# 215.py test cases
import pytest
import p215

# Test generate_rows
def test_generate_rows_0():
	p215.generate_rows([],2)
	assert p215.rows == [(2,)]

def test_generate_rows_1():
	p215.rows = []
	p215.generate_rows([],3)
	assert p215.rows == [(3,)]

def test_generate_rows_2():
	p215.rows = []
	p215.generate_rows([],4)
	assert p215.rows == [(2,2)]

def test_generate_rows_3():
	p215.rows = []
	p215.generate_rows([],5)
	assert p215.rows == [(2,3), (3,2)]


# Test is_solution
def test_is_solution_0():
	assert p215.is_solution([(2,3),(3,2)]) == True

def test_is_solution_1():
	assert p215.is_solution([(2,2),(2,2)]) == False

def test_is_solution_2():
	assert p215.is_solution([(2,2,3),(2,2,3)]) == False

def test_is_solution_3():
	assert p215.is_solution([(3,2,3,2),(3,2,3,2)]) == False

def test_is_solution_4():
	assert p215.is_solution([(2,3,2,2),(3,3,3)]) == True

def test_is_solution_4():
	assert p215.is_solution([(2,3,2,2),(3,3,3),(2,3,2,2)]) == True
