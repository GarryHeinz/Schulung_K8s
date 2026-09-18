package de.ordix.devops.todos.model;

import jakarta.persistence.AttributeConverter;
import jakarta.persistence.Converter;

/**
 * JOA Attribute Converter
 * @author ngj
 */
@Converter(autoApply = true)
public class PriorityAttributeConverter  
	implements AttributeConverter<Priority, String>{

    @Override
    public String convertToDatabaseColumn(Priority attribute) {
	if(null == attribute){
	    return null;
	}
	return attribute.name();
    }

    @Override
    public Priority convertToEntityAttribute(String dbData) {
	if(null == dbData){
	    return null;
	}
	return switch (dbData.toLowerCase()) {
	    case "low" -> Priority.LOW;
	    case "normal" -> Priority.NORMAL;
	    case "high" -> Priority.HIGH;
	    default -> null;
	};
    }
    
}
