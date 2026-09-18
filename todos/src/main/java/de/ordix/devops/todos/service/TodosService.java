package de.ordix.devops.todos.service;

import de.ordix.devops.todos.model.Todo;
import de.ordix.devops.todos.repository.TodosRepository;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Todo Service
 * @author ngj
 */
@Service
public class TodosService {
    
    private final TodosRepository repository;
    
    @Autowired
    public TodosService(TodosRepository repo){
	this.repository = repo;
    }
    
    public List<Todo> findAll(){
	return repository.findAll();
    }

    public void save(Todo todo){
        repository.save(todo);
    }
}
