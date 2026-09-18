package de.ordix.devops.todos;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * Info about Pod receiving current incoming Request 
 *
 * @author ngj
 */
@RestController
@RequestMapping("/infos")
public class K8sInfoController {

    @Value("${POD_NAME:UNKNOWN_POD_NAME}")
    private String podName;
    @Value("${POD_NAMESPACE:UNKNOWN_POD_NAMESPACE}")
    private String podNamespace;
    @Value("${POD_IP:UNKNOWN_POD_IP}")
    private String podIp;
    @Value("${NODE_NAME:UNKNOWN_NODE}")
    private String nodeName;

    @GetMapping("/")
    public String getK8sPodInfos() {
	return String.format("REQUEST served from POD: %s/%s %s K8s-Cluster: %s", 
		podName, podNamespace, podIp, nodeName);
    }

}
