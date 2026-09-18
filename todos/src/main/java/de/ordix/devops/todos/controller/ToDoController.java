package de.ordix.devops.todos.controller;

import de.ordix.devops.todos.model.Todo;
import de.ordix.devops.todos.service.TodosService;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;

@RestController
@RequestMapping("/todos")
public class ToDoController {

    private final TodosService service;
    
    @Autowired
    public ToDoController(TodosService srvc){
	this.service = srvc;
    }

    @GetMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public List<Todo> checkStatus() {
        return service.findAll();
    }

    @PostMapping(consumes = MediaType.APPLICATION_JSON_VALUE)
    public void addTodo(@RequestBody Todo todo) {
        service.save(todo);
    }

}
