$TTL	86400
@	IN	SOA	localhost. root.localhost. (
			      1		; Serial
			 604800		; Refresh
			  86400		; Retry
			2419200		; Expire
			  86400 )	; Negative Cache TTL
;
    IN  A   172.17.0.1
@	IN	NS	localhost.
