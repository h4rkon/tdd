package com.example.gameoflife;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


class RulesTests {

	@Test
	void ReturnTrue_GetsCalled_ReturnsTrue() {
		// arrange
		Rules demoClass = new Rules();

		//act
		boolean actual = demoClass.ReturnTrue();

		//assert
		Assertions.assertTrue(actual);
	}

}
