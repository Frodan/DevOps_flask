terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

}

provider "aws" {
  profile = "default"
  region  = "eu-central-1"
}

resource "aws_instance" "app" {
  ami           = "ami-0b1deee75235aa4bb"
  instance_type = "t2.micro"

  tags = {
    Name = "AWS App server"
  }
}