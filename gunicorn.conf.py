# number of processes to create
workers = 1

worker_class = 'uvicorn.workers.UvicornWorker'

# tasks may run for up to 60 seconds
timeout = 60

# the number of requests a worker may execute before gracefully reloading (to clear memory etc)
max_requests = 10

# random offset between 0 and 10 after max_requests.  So that all workers don't stop at the same time.
max_requests_jitter = 5

# compile the processes code and distribute that to workers (reduce startup time and show startup errors)
preload = True

# applications will know that the request was sent over HTTPS
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
