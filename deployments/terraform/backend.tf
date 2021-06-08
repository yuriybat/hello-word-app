terraform {
  backend "gcs" {
    bucket  = "ybbucket912"
    prefix  = "qa/hello-world"
    project = "meta-map-315419"
  }
}
