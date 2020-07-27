###   MODULE   ###
variable "stage" {
  description = "Deployment type"
  type = string
  default = "dev"
}

variable "project" {
  description = "Project name"
  type = string
}

variable "namespace" {
  description = "Module namespace"
  type = string
}

variable "region" {
  description = "Availability region"
  type = string
}

variable "hosted_zone_id" {
  description = "Your route 53 hosted zone ID for the domain you want to link the instance to"
  type = string
}
