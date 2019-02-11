#!/usr/bin/env bash


__main__ ()
{


	local THE_URL_SEARH='https://www.googleapis.com/youtube/v3/search'
	local THE_OPT_KEY='?key={YOUR_API_KEY}'
	local THE_OPT_PART='&part=snippet'
	local THE_OPT_TYPE='&type=video'
	local THE_OPT_MAX_RESULTS='&maxResults=10'
	local THE_OPT_ORDER='&order=relevance'
	local THE_OPT_PRETTY_PRINT='&prettyPrint=false'
	local THE_OPT_KEYWORD='&q=black%20bird'

	local TEH_API_URL="$THE_URL_SEARH$THE_OPT_KEY$THE_OPT_PART$THE_OPT_TYPE$THE_OPT_MAX_RESULTS$THE_OPT_ORDER$THE_OPT_PRETTY_PRINT$THE_OPT_KEYWORD"

	#echo "$TEH_API_URL" ## https://www.googleapis.com/youtube/v3/search?key={YOUR_API_KEY}&part=snippet&type=video&maxResults=10&order=relevance&prettyPrint=false&q=black%20bird

	curl -s "$TEH_API_URL"
}

__main__
