package com.hsbg.hello;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.ec2.AmazonEC2;
import com.amazonaws.services.ec2.AmazonEC2ClientBuilder;
import com.amazonaws.services.ec2.model.CreateTagsRequest;
import com.amazonaws.services.ec2.model.Instance;
import com.amazonaws.services.ec2.model.InstanceNetworkInterfaceSpecification;
import com.amazonaws.services.ec2.model.RunInstancesRequest;
import com.amazonaws.services.ec2.model.RunInstancesResult;
import com.amazonaws.services.ec2.model.StartInstancesRequest;
import com.amazonaws.services.ec2.model.Tag;

/**
 * Servlet implementation class HelloServlet
 */
@WebServlet("/ec2Servlet")
public class HelloServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	private static final AWSCredentials AWS_CREDENTIALS;
    
    static {
        // Your accesskey and secretkey
        AWS_CREDENTIALS = new BasicAWSCredentials(
                "Change me",
                "Change me"
        );
	
	}
    /**
     * @see HttpServlet#HttpServlet()
     */
    public HelloServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    
	        // Set up the amazon ec2 client
        AmazonEC2 ec2Client = AmazonEC2ClientBuilder.standard()
                .withCredentials(new AWSStaticCredentialsProvider(AWS_CREDENTIALS))
                .withRegion(Regions.US_EAST_2)
                .build();
         
        // Launch an Amazon EC2 Instance
        RunInstancesRequest runInstancesRequest = new RunInstancesRequest().withImageId("ami-05bfbece1ed5beb54")
                .withInstanceType("t2.micro") // https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html
                .withMinCount(1)
                .withMaxCount(1)
                .withKeyName("vilas")
                .withNetworkInterfaces(new InstanceNetworkInterfaceSpecification()
                        .withAssociatePublicIpAddress(true)
                        .withDeviceIndex(0)
                        .withSubnetId("subnet-286f7340"));
 
        RunInstancesResult runInstancesResult = ec2Client.runInstances(runInstancesRequest);
 
        Instance instance = runInstancesResult.getReservation().getInstances().get(0);
        String instanceId = instance.getInstanceId();
        System.out.println("EC2 Instance Id: " + instanceId);
 
        // Setting up the tags for the instance
        CreateTagsRequest createTagsRequest = new CreateTagsRequest()
                .withResources(instance.getInstanceId())
                .withTags(new Tag("Name", "VilasTest"));
        ec2Client.createTags(createTagsRequest);
 
        // Starting the Instance
        StartInstancesRequest startInstancesRequest = new StartInstancesRequest().withInstanceIds(instanceId);
 
        ec2Client.startInstances(startInstancesRequest);



		PrintWriter writer = response.getWriter();
		writer.println("<h1>Created " + instanceId + "</h1>");
		writer.close();
	}

}
