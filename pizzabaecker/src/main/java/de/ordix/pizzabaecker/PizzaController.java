package de.ordix.pizzabaecker;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/")
public class PizzaController {

    private String[] pizzas = {
        "Magharita",
        "Salamie",
        "Speciale",
        "Thunfisch",
        "Schinken"
    };

    @GetMapping
    public String getPizzas() {
        String html = "<h1>Meine Pizzas:</h1>";
        for (String pizza : pizzas) 
            html += "+ " + pizza + "<br />";
        html += "<p>Hostname: " + System.getenv("HOSTNAME") + "</p>";
        return html;
    }

}
