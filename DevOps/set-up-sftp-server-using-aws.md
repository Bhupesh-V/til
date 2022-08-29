# Set up a SFTP server using AWS Transfer Family
**_Posted on 04 Aug, 2022_**


## Step 1: Set up a SFTP server (optional)

We will be using the AWS Transfer family to setup a fully managed SFTP server. During the whole process if you face any issues while setting up, visit the troubleshoot guide. With AWS Transfer family we can use a S3 bucket to host our files.

### Step 1.1 Create a AWS S3 Bucket

1. Sign in to the AWS Management Console and open the Amazon S3 console at https://console.aws.amazon.com/s3/. Choose **Create bucket**.
2. In Bucket name, enter a DNS-compliant name for your bucket. Make sure to read bucket naming rules.
3. In Region, choose the AWS Region, choose a Region close to you to minimize latency and costs and address regulatory requirements.
4. Choose the recommended option for **Object Ownership**.
5. Block all public access.
6. Optionally your can choose to add any tags.
7. Choose **Create bucket**.

### Step 1.2 Create an IAM policy for AWS Transfer Family

1. Open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, choose **Policies**, and then choose **Create policy**.
3. On the Create Policy page, choose the JSON tab.
4. In the editor that appears, replace the contents of the editor with following.
   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Sid": "VisualEditor0",
               "Effect": "Allow",
               "Action": [
                   "s3:ListBucket",
                   "s3:GetBucketLocation"
               ],
               "Resource": "arn:aws:s3:::MYBUCKET"
           },
           {
               "Sid": "VisualEditor1",
               "Effect": "Allow",
               "Action": [
                   "s3:PutObject",
                   "s3:GetObject",
                   "s3:DeleteObject"
               ],
               "Resource": "arn:aws:s3:::MYBUCKET/*"
           },
           {
               "Sid": "VisualEditor2",
               "Effect": "Allow",
               "Action": "transfer:*",
               "Resource": "*"
           }
       ]
   }
   ```
5. Choose Review policy and provide a name and description for your policy, and then choose **Create policy**.


### Step 1.3 Create an IAM Role

Next, we create an IAM role and attach the new created IAM policy to it.

1. In the navigation pane, choose Roles, and then choose Create role. On the Create role page, make sure that AWS service is chosen.
2. Choose Transfer from the service list, and then choose Next: Permissions. This establishes a trust relationship between AWS Transfer Family and AWS.
3. In the Attach permissions policies section, locate and choose the policy that you just created (reload the policies if you can’t find the one you created), and choose Next: **Tags**.
4. (Optional) Enter a key and value for a tag, and choose Next: **Review**.
5. On the Review page, enter a name and description for your new role, and then choose **Create role**.


### Step 1.4 Create a SFTP server

1. When configuring your new server, choose the protocol (SFTP, FTPS, or FTP).
2. In the next step, you’ll be able to set up the identity provider manager for user authentication and authorization. The user permissions will be enforced by an associated AWS role in the IAM (Identity & Access Management) service, but you can also provide a custom identity provider via the API.
3. Next, configure endpoints (whether the resources will be reachable from the Internet or via a VPC and its hostname).
4. In Domain, choose `S3` as the default AWS Storage service. Choose to Configure any additional services, then review, and create your server.


After everything is done, you will see a dashboard like this. Our SFTP server is up and running, although it can’t be accessed because it has no users. Click on the server ID, and click on “Add User.”

### Step 1.5 Create a AWS user

1. For username, pick anything memorable.
2. In Roles option, pick the role we created in previous Step 1.3
3. Attach the policy we created in Step 1.2
4. For Home Directory, choose the name of S3 bucket we created in Step 1.1.
5. To Generate a SSH Public key, we will use the following command,
   ```bash
   ssh-keygen -t rsa -b 4096
   ```
6. Once you create the key, your public key will be available in `$HOME/.ssh/id_rsa.pub`, copy the file contents and add it in the SSH Public Key field.
7. You can now log-in to your server using a SFTP client. We will be using OpenSSH. You can find documentation for different SFTP client on AWS.


Use the following command to start a client connection to the server.

```bash
sftp your-username@endpoint.amazonaws.com
```

Once you login, a `sftp>` prompt should appear. Enjoy your personal SFTP file server
