package de.ordix.pizzabaecker;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class PizzabaeckerApplicationTests {

	@Autowired
	PizzaController pizzaController;

	@Test
	void contextLoads() {
	}

	@Test
	void shouldShowPizzas() {
		assertTrue(pizzaController.getPizzas().length() > 0);
	}

}
