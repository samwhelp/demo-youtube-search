#!/usr/bin/env php
<?php

	$input = file_get_contents("php://stdin");

	var_dump(json_decode($input, true));
