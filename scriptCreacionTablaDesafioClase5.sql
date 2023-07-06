create table company_earnings(
		actual decimal(8,5),
		estimate decimal(8,5),
		periodo date,
		cuarto int,
		surprise decimal(8,5),
		surprisePercent decimal(8,5),
		symbol varchar(15) DISTKEY,   
		anio int 
	) SORTKEY (anio)
