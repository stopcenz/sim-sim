# -*- coding: utf-8 -*- 
home_page = u"""<!DOCTYPE html>
<html lang="ru"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>%%host%% - Вебпрокси</title>
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<meta name="description" content="Anonimizer, Web-Based Proxy">
<link rel="canonical" href="https://%%host%%/">
<link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Roboto:400,700">
<link rel=icon type="image/png" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyRpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuMy1jMDExIDY2LjE0NTY2MSwgMjAxMi8wMi8wNi0xNDo1NjoyNyAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENTNiAoTWFjaW50b3NoKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpFN0NDQkZGOTg5RkYxMUU2OEY2QjhCNzZEQzAxMUVCMiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpFN0NDQkZGQTg5RkYxMUU2OEY2QjhCNzZEQzAxMUVCMiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkU3Q0NCRkY3ODlGRjExRTY4RjZCOEI3NkRDMDExRUIyIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkU3Q0NCRkY4ODlGRjExRTY4RjZCOEI3NkRDMDExRUIyIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+QV3sowAAADBQTFRFDgsH9+VN788227kz7/f5+O5+1+/5qZAzlpZyx7dXztLMssPGgXI31N/o6OzlwL2IBpP4HwAAAIhJREFUeNpMj1ESxCAIQ2lioVi097/tgut29n04JiGjiBTXmVzyw86NfbWfL77y44+aOXAQJcC81gBAcyeNQI7kCXi/uyEjUMDHvY05uq1M4K3Plo5GLIOurZjDuSq2jTZXJd99VMsaYashEjrSmSEGIuqrd1MdlpLYy1z3Y5aS8e4bqbf8CDAAGawETgK4fNoAAAAASUVORK5CYII=">

<style> <!-- main.css -->

/* Reset */

	html, body, div, span, applet, object, iframe, h1, h2, h3, h4, h5, h6, p, blockquote, pre, a, abbr, acronym, address, big, cite, code, del, dfn, em, img, ins, kbd, q, s, samp, small, strike, strong, sub, sup, tt, var, b, u, i, center, dl, dt, dd, ol, ul, li, fieldset, form, label, legend, table, caption, tbody, tfoot, thead, tr, th, td, article, aside, canvas, details, embed, figure, figcaption, footer, header, hgroup, menu, nav, output, ruby, section, summary, time, mark, audio, video {
		margin: 0;
		padding: 0;
		border: 0;
		font-size: 100%;
		font: inherit;
		vertical-align: baseline;
	}

	article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section {
		display: block;
	}

	body {
		line-height: 1;
	}

	ol, ul {
		list-style: none;
	}

	blockquote, q {
		quotes: none;
	}

	blockquote:before, blockquote:after, q:before, q:after {
		content: '';
		content: none;
	}

	table {
		border-collapse: collapse;
		border-spacing: 0;
	}

	body {
		-webkit-text-size-adjust: none;
	}

/* Box Model */

	*, *:before, *:after {
		-moz-box-sizing: border-box;
		-webkit-box-sizing: border-box;
		box-sizing: border-box;
	}

/* Basic */

	@-ms-viewport {
		width: device-width;
	}

	body {
		-ms-overflow-style: scrollbar;
	}

	@media screen and (max-width: 480px) {

		html, body {
			min-width: 320px;
		}

	}

	html, body {
		height: 100%;
		overflow-x: hidden;
		width: 100%;
	}

		@media screen and (max-height: 640px) {

			html, body {
				height: auto;
				min-height: 100%;
			}

		}

	body {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		-moz-flex-direction: column;
		-webkit-flex-direction: column;
		-ms-flex-direction: column;
		flex-direction: column;
		-moz-justify-content: center;
		-webkit-justify-content: center;
		-ms-justify-content: center;
		justify-content: center;
		background-color: #fff;
		padding: 6em 4em 4em 4em;
	}

		body > * {
			position: relative;
			z-index: 2;
		}

		body.is-loading *, body.is-loading *:before, body.is-loading *:after {
			-moz-animation: none !important;
			-webkit-animation: none !important;
			-ms-animation: none !important;
			animation: none !important;
			-moz-transition: none !important;
			-webkit-transition: none !important;
			-ms-transition: none !important;
			transition: none !important;
		}

		@media screen and (max-width: 1680px) {

			body {
				padding: 6em 3.5em 3.5em 3.5em;
			}

		}

		@media screen and (max-width: 736px) {

			body {
				padding: 5em 2em 2em 2em;
			}

		}

		@media screen and (max-width: 360px) {

			body {
				padding: 5em 1.25em 1.25em 1.25em;
			}

		}

/* BG */

	#bg {
		-moz-transition: opacity 2s ease-in-out;
		-webkit-transition: opacity 2s ease-in-out;
		-ms-transition: opacity 2s ease-in-out;
		transition: opacity 2s ease-in-out;
		height: 100%;
		left: 0;
		opacity: 0.25;
		position: fixed;
		top: 0;
		width: 100%;
		z-index: 1;
	}

		#bg div {
			-moz-transition: opacity 3s ease, visibility 3s;
			-webkit-transition: opacity 3s ease, visibility 3s;
			-ms-transition: opacity 3s ease, visibility 3s;
			transition: opacity 3s ease, visibility 3s;
			background-size: cover;
			height: 100%;
			left: 0;
			opacity: 0;
			position: absolute;
			top: 0;
			visibility: hidden;
			width: 150%;
		}

			#bg div.visible {
				-moz-animation: bg 45s linear infinite;
				-webkit-animation: bg 45s linear infinite;
				-ms-animation: bg 45s linear infinite;
				animation: bg 45s linear infinite;
				opacity: 1;
				visibility: visible;
				z-index: 1;
			}

				#bg div.visible.top {
					z-index: 2;
				}

				@media screen and (max-width: 1280px) {

					#bg div.visible {
						-moz-animation: bg 29.25s linear infinite;
						-webkit-animation: bg 29.25s linear infinite;
						-ms-animation: bg 29.25s linear infinite;
						animation: bg 29.25s linear infinite;
					}

				}

				@media screen and (max-width: 736px) {

					#bg div.visible {
						-moz-animation: bg 18s linear infinite;
						-webkit-animation: bg 18s linear infinite;
						-ms-animation: bg 18s linear infinite;
						animation: bg 18s linear infinite;
					}

				}

			#bg div:only-child {
				-moz-animation-direction: alternate !important;
				-webkit-animation-direction: alternate !important;
				-ms-animation-direction: alternate !important;
				animation-direction: alternate !important;
			}

		body.is-loading #bg {
			opacity: 0;
		}

	@-moz-keyframes bg {
		0% {
			-moz-transform: translateX(0);
			-webkit-transform: translateX(0);
			-ms-transform: translateX(0);
			transform: translateX(0);
		}

		100% {
			-moz-transform: translateX(-25%);
			-webkit-transform: translateX(-25%);
			-ms-transform: translateX(-25%);
			transform: translateX(-25%);
		}
	}

	@-webkit-keyframes bg {
		0% {
			-moz-transform: translateX(0);
			-webkit-transform: translateX(0);
			-ms-transform: translateX(0);
			transform: translateX(0);
		}

		100% {
			-moz-transform: translateX(-25%);
			-webkit-transform: translateX(-25%);
			-ms-transform: translateX(-25%);
			transform: translateX(-25%);
		}
	}

	@-ms-keyframes bg {
		0% {
			-moz-transform: translateX(0);
			-webkit-transform: translateX(0);
			-ms-transform: translateX(0);
			transform: translateX(0);
		}

		100% {
			-moz-transform: translateX(-25%);
			-webkit-transform: translateX(-25%);
			-ms-transform: translateX(-25%);
			transform: translateX(-25%);
		}
	}

	@keyframes bg {
		0% {
			-moz-transform: translateX(0);
			-webkit-transform: translateX(0);
			-ms-transform: translateX(0);
			transform: translateX(0);
		}

		100% {
			-moz-transform: translateX(-25%);
			-webkit-transform: translateX(-25%);
			-ms-transform: translateX(-25%);
			transform: translateX(-25%);
		}
	}

/* Type */

	body, input, select, textarea {
		color: rgba(0, 0, 0, 0.75);
		font-family: "Roboto", sans-serif;
		font-size: 16pt;
		font-weight: 400;
		letter-spacing: -0.01em;
		line-height: 1.65em;
	}

		@media screen and (max-width: 1680px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 1280px) {

			body, input, select, textarea {
				font-size: 11pt;
			}

		}

		@media screen and (max-width: 980px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 736px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

		@media screen and (max-width: 480px) {

			body, input, select, textarea {
				font-size: 12pt;
			}

		}

	a {
		-moz-transition: border-bottom-color 0.2s ease, color 0.2s ease;
		-webkit-transition: border-bottom-color 0.2s ease, color 0.2s ease;
		-ms-transition: border-bottom-color 0.2s ease, color 0.2s ease;
		transition: border-bottom-color 0.2s ease, color 0.2s ease;
		border-bottom: dotted 1px rgba(0, 0, 0, 0.25);
		color: #1cb495;
		text-decoration: none;
	}

		a:hover {
			border-bottom-color: transparent;
			color: #1cb495 !important;
			text-decoration: none;
		}

	strong, b {
		color: #000;
		font-weight: 700;
	}

	em, i {
		font-style: italic;
	}

	p {
		margin: 0 0 2em 0;
	}

	h1, h2, h3, h4, h5, h6 {
		color: #000;
		font-weight: 700;
		line-height: 1em;
		margin: 0 0 1em 0;
	}

		h1 a, h2 a, h3 a, h4 a, h5 a, h6 a {
			color: inherit;
			text-decoration: none;
		}

	h1 {
		font-size: 2.5em;
		line-height: 1.25em;
	}

	h2 {
		font-size: 1.75em;
		line-height: 1.5em;
	}

	h3 {
		font-size: 1.35em;
		line-height: 1.5em;
	}

	h4 {
		font-size: 1.1em;
		line-height: 1.5em;
	}

	h5 {
		font-size: 0.9em;
		line-height: 1.5em;
	}

	h6 {
		font-size: 0.7em;
		line-height: 1.5em;
	}

	sub {
		font-size: 0.8em;
		position: relative;
		top: 0.5em;
	}

	sup {
		font-size: 0.8em;
		position: relative;
		top: -0.5em;
	}

	blockquote {
		border-left: solid 8px rgba(255, 255, 255, 0.35);
		font-style: italic;
		margin: 0 0 2em 0;
		padding: 0.5em 0 0.5em 2em;
	}

	code {
		background: rgba(255, 255, 255, 0.125);
		border-radius: 6px;
		border: solid 2px rgba(255, 255, 255, 0.35);
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0.25em;
		padding: 0.25em 0.65em;
	}

	pre {
		-webkit-overflow-scrolling: touch;
		font-family: "Courier New", monospace;
		font-size: 0.9em;
		margin: 0 0 2em 0;
	}

		pre code {
			display: block;
			line-height: 1.75em;
			padding: 1em 1.5em;
			overflow-x: auto;
		}

	hr {
		border: 0;
		border-bottom: solid 2px rgba(255, 255, 255, 0.35);
		margin: 2em 0;
	}

		hr.major {
			margin: 3em 0;
		}

/* Section/Article */

	section.special, article.special {
		text-align: center;
	}

	header p {
		color: rgba(0, 0, 0, 0.5);
		position: relative;
		margin: 0 0 1.5em 0;
	}

	header h2 + p {
		font-size: 1.25em;
		margin-top: -1em;
		line-height: 1.5em;
	}

	header h3 + p {
		font-size: 1.1em;
		margin-top: -0.8em;
		line-height: 1.5em;
	}

	header h4 + p,
	header h5 + p,
	header h6 + p {
		font-size: 0.9em;
		margin-top: -0.6em;
		line-height: 1.5em;
	}

	@media screen and (max-width: 980px) {

		header br {
			display: none;
		}

	}

	@media screen and (max-width: 736px) {

		header br {
			display: inline;
		}

	}

	@media screen and (max-width: 480px) {

		header br {
			display: none;
		}

	}

/* Icon */

	.icon {
		text-decoration: none;
		border-bottom: none;
		position: relative;
	}

		.icon:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			font-family: FontAwesome;
			font-style: normal;
			font-weight: normal;
			text-transform: none !important;
		}

		.icon > .label {
			display: none;
		}

/* List */

	ol {
		list-style: decimal;
		margin: 0 0 2em 0;
		padding-left: 1.25em;
	}

		ol li {
			padding-left: 0.25em;
		}

	ul {
		list-style: disc;
		margin: 0 0 2em 0;
		padding-left: 1em;
	}

		ul li {
			padding-left: 0.5em;
		}

		ul.icons {
			cursor: default;
			list-style: none;
			padding-left: 0;
		}

			ul.icons li {
				display: inline-block;
				padding: 0 1em 0 0;
			}

				ul.icons li:last-child {
					padding-right: 0;
				}

				ul.icons li .icon:before {
					font-size: 1.25em;
				}

				ul.icons li a {
					color: inherit;
				}

/* Form */

	form {
		margin: 0 0 2em 0;
	}

		form .message {
			text-decoration: none;
			-moz-transition: opacity 0.2s ease-in-out, -moz-transform 0.2s ease-in-out;
			-webkit-transition: opacity 0.2s ease-in-out, -webkit-transform 0.2s ease-in-out;
			-ms-transition: opacity 0.2s ease-in-out, -ms-transform 0.2s ease-in-out;
			transition: opacity 0.2s ease-in-out, transform 0.2s ease-in-out;
			-moz-transform: scale(1.05);
			-webkit-transform: scale(1.05);
			-ms-transform: scale(1.05);
			transform: scale(1.05);
			height: 2.75em;
			line-height: 2.75em;
			opacity: 0;
		}

			form .message:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				font-family: FontAwesome;
				font-style: normal;
				font-weight: normal;
				text-transform: none !important;
			}

			form .message:before {
				margin-right: 0.5em;
			}

			form .message.visible {
				-moz-transform: scale(1);
				-webkit-transform: scale(1);
				-ms-transform: scale(1);
				transform: scale(1);
				opacity: 1;
			}

			form .message.success {
				color: #1cb495;
			}

				form .message.success:before {
					content: '\f00c';
				}

			form .message.failure {
				color: #ff2361;
			}

				form .message.failure:before {
					content: '\f119';
				}

	label {
		color: #000;
		display: block;
		font-size: 0.9em;
		font-weight: 700;
		margin: 0 0 1em 0;
	}

	@-moz-keyframes focus {
		0% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}

		50% {
			-moz-transform: scale(1.025);
			-webkit-transform: scale(1.025);
			-ms-transform: scale(1.025);
			transform: scale(1.025);
		}

		100% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}
	}

	@-webkit-keyframes focus {
		0% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}

		50% {
			-moz-transform: scale(1.025);
			-webkit-transform: scale(1.025);
			-ms-transform: scale(1.025);
			transform: scale(1.025);
		}

		100% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}
	}

	@-ms-keyframes focus {
		0% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}

		50% {
			-moz-transform: scale(1.025);
			-webkit-transform: scale(1.025);
			-ms-transform: scale(1.025);
			transform: scale(1.025);
		}

		100% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}
	}

	@keyframes focus {
		0% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}

		50% {
			-moz-transform: scale(1.025);
			-webkit-transform: scale(1.025);
			-ms-transform: scale(1.025);
			transform: scale(1.025);
		}

		100% {
			-moz-transform: scale(1);
			-webkit-transform: scale(1);
			-ms-transform: scale(1);
			transform: scale(1);
		}
	}

	input[type="url"],
	input[type="text"],
	input[type="password"],
	input[type="email"],
	select,
	textarea {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transform: scale(1);
		-webkit-transform: scale(1);
		-ms-transform: scale(1);
		transform: scale(1);
		-moz-transition: border-color 0.2s ease, background-color 0.2s ease;
		-webkit-transition: border-color 0.2s ease, background-color 0.2s ease;
		-ms-transition: border-color 0.2s ease, background-color 0.2s ease;
		transition: border-color 0.2s ease, background-color 0.2s ease;
		background-color: transparent;
		border-radius: 6px;
		border: none;
		border: solid 2px rgba(0, 0, 0, 0.35);
		color: inherit;
		display: block;
		outline: 0;
		padding: 0 1em;
		text-decoration: none;
		width: 100%;
	}

		input[type="url"]:invalid,
		input[type="text"]:invalid,
		input[type="password"]:invalid,
		input[type="email"]:invalid,
		select:invalid,
		textarea:invalid {
			box-shadow: none;
		}

		input[type="url"]:focus,
		input[type="text"]:focus,
		input[type="password"]:focus,
		input[type="email"]:focus,
		select:focus,
		textarea:focus {
			-moz-animation: focus 0.1s;
			-webkit-animation: focus 0.1s;
			-ms-animation: focus 0.1s;
			animation: focus 0.1s;
			background-color: rgba(0, 0, 0, 0.125);
			border-color: #1cb495;
		}

	.select-wrapper {
		text-decoration: none;
		display: block;
		position: relative;
	}

		.select-wrapper:before {
			-moz-osx-font-smoothing: grayscale;
			-webkit-font-smoothing: antialiased;
			font-family: FontAwesome;
			font-style: normal;
			font-weight: normal;
			text-transform: none !important;
		}

		.select-wrapper:before {
			color: rgba(0, 0, 0, 0.35);
			content: '\f078';
			display: block;
			height: 2.75em;
			line-height: 2.75em;
			pointer-events: none;
			position: absolute;
			right: 0;
			text-align: center;
			top: 0;
			width: 2.75em;
		}

		.select-wrapper select::-ms-expand {
			display: none;
		}

	input[type="url"],
	input[type="text"],
	input[type="password"],
	input[type="email"],
	select {
		height: 2.75em;
	}

	textarea {
		padding: 0.75em 1em;
	}

	input[type="checkbox"],
	input[type="radio"] {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		display: block;
		float: left;
		margin-right: -2em;
		opacity: 0;
		width: 1em;
		z-index: -1;
	}

		input[type="checkbox"] + label,
		input[type="radio"] + label {
			text-decoration: none;
			color: rgba(255, 255, 255, 0.75);
			cursor: pointer;
			display: inline-block;
			font-size: 1em;
			font-weight: 400;
			padding-left: 2.4em;
			padding-right: 0.75em;
			position: relative;
		}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				-moz-osx-font-smoothing: grayscale;
				-webkit-font-smoothing: antialiased;
				font-family: FontAwesome;
				font-style: normal;
				font-weight: normal;
				text-transform: none !important;
			}

			input[type="checkbox"] + label:before,
			input[type="radio"] + label:before {
				background: rgba(255, 255, 255, 0.125);
				border-radius: 6px;
				border: solid 2px rgba(255, 255, 255, 0.35);
				content: '';
				display: inline-block;
				height: 1.65em;
				left: 0;
				line-height: 1.58125em;
				position: absolute;
				text-align: center;
				top: 0;
				width: 1.65em;
			}

		input[type="checkbox"]:checked + label:before,
		input[type="radio"]:checked + label:before {
			background: #1cb495;
			border-color: #1cb495;
			color: #ffffff;
			content: '\f00c';
		}

		input[type="checkbox"]:focus + label:before,
		input[type="radio"]:focus + label:before {
			border-color: #1cb495;
			box-shadow: 0 0 0 2px #1cb495;
		}

	input[type="checkbox"] + label:before {
		border-radius: 6px;
	}

	input[type="radio"] + label:before {
		border-radius: 100%;
	}

	::-webkit-input-placeholder {
		color: rgba(0, 0, 0, 0.5) !important;
		opacity: 1.0;
	}

	:-moz-placeholder {
		color: rgba(0, 0, 0, 0.5) !important;
		opacity: 1.0;
	}

	::-moz-placeholder {
		color: rgba(0, 0, 0, 0.5) !important;
		opacity: 1.0;
	}

	:-ms-input-placeholder {
		color: rgba(0, 0, 0, 0.5) !important;
		opacity: 1.0;
	}

	.formerize-placeholder {
		color: rgba(0, 0, 0, 0.5) !important;
		opacity: 1.0;
	}

/* Button */

	input[type="submit"],
	input[type="reset"],
	input[type="button"],
	button,
	.button {
		-moz-appearance: none;
		-webkit-appearance: none;
		-ms-appearance: none;
		appearance: none;
		-moz-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		-webkit-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		-ms-transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		transition: background-color 0.2s ease-in-out, color 0.2s ease-in-out, opacity 0.2s ease-in-out;
		background-color: #1cb495;
		border-radius: 6px;
		border: 0;
		color: #ffffff !important;
		cursor: pointer;
		display: inline-block;
		font-weight: 700;
		height: 2.75em;
		line-height: 2.75em;
		padding: 0 1.125em;
		text-align: center;
		text-decoration: none;
		white-space: nowrap;
	}

		input[type="submit"]:hover,
		input[type="reset"]:hover,
		input[type="button"]:hover,
		button:hover,
		.button:hover {
			background-color: #1fcaa7;
		}

		input[type="submit"]:active,
		input[type="reset"]:active,
		input[type="button"]:active,
		button:active,
		.button:active {
			background-color: #199e83;
		}

		input[type="submit"].disabled, input[type="submit"]:disabled,
		input[type="reset"].disabled,
		input[type="reset"]:disabled,
		input[type="button"].disabled,
		input[type="button"]:disabled,
		button.disabled,
		button:disabled,
		.button.disabled,
		.button:disabled {
			opacity: 0.5;
		}

		@media screen and (max-width: 480px) {

			input[type="submit"],
			input[type="reset"],
			input[type="button"],
			button,
			.button {
				padding: 0;
			}
		}

/* Header */

	#header h1 {
		font-size: 3.25em;
		margin: 0 0 0.55em 0;
	}

	#header p {
		font-size: 1.35em;
		line-height: 1.65em;
	}

	#header a {
		color: inherit;
	}

	@media screen and (max-width: 736px) {

		#header h1 {
			font-size: 2em;
		}

		#header p {
			font-size: 1em;
		}
	}

	@media screen and (max-width: 480px) {

		#header {
			margin: 0 0 1em 0;
		}
	}

/* Signup Form */

	#signup-form {
		display: -moz-flex;
		display: -webkit-flex;
		display: -ms-flex;
		display: flex;
		position: relative;
	}

		#signup-form input[type="url"],
		#signup-form input[type="text"],
		#signup-form input[type="password"],
		#signup-form input[type="email"] {
			width: 18em;
		}

		#signup-form > * {
			margin: 0 0 0 1em;
		}

		#signup-form > :first-child {
			margin: 0 0 0 0;
		}

		@media screen and (max-width: 480px) {

			#signup-form {
				-moz-flex-direction: column;
				-webkit-flex-direction: column;
				-ms-flex-direction: column;
				flex-direction: column;
			}

				#signup-form input[type="type"],
				#signup-form input[type="password"],
				#signup-form input[type="email"] {
					width: 100%;
				}

				#signup-form > * {
					margin: 1.25em 0 0 0;
				}

				#signup-form .message {
					bottom: -1.5em;
					font-size: 0.9em;
					height: 1em;
					left: 0;
					line-height: inherit;
					margin-top: 0;
					position: absolute;
				}
		}

/* Footer */

	#footer {
		-moz-transition: opacity 0.5s ease-in-out;
		-webkit-transition: opacity 0.5s ease-in-out;
		-ms-transition: opacity 0.5s ease-in-out;
		transition: opacity 0.5s ease-in-out;
		bottom: 4em;
		color: rgba(0, 0, 0, 0.5);
		left: 4em;
		opacity: 0.5;
		position: absolute;
	}

		#footer .icons {
			margin: 0 0 0.5em 0;
		}

		#footer .copyright {
			font-size: 0.8em;
			list-style: none;
			padding: 0;
		}

			#footer .copyright li {
				border-left: solid 1px rgba(255, 255, 255, 0.25);
				display: inline-block;
				line-height: 1em;
				margin: 0 0 0 0.75em;
				padding: 0 0 0 0.75em;
			}

				#footer .copyright li:first-child {
					border-left: 0;
					margin-left: 0;
					padding-left: 0;
				}

			#footer .copyright a {
				color: inherit;
			}

		#footer:hover {
			opacity: 1;
		}

		#footer > :last-child {
			margin-bottom: 0;
		}

		@media screen and (max-width: 1680px) {

			#footer {
				bottom: 3.5em;
				left: 3.5em;
			}
		}

		@media screen and (max-width: 736px) {

			#footer {
				bottom: 2em;
				left: 2em;
			}
		}

		@media screen and (max-width: 360px) {

			#footer {
				bottom: 1.25em;
				left: 1.25em;
			}
		}

		@media screen and (max-height: 640px) {

			#footer {
				bottom: auto;
				left: auto;
				margin: 1em 0 0 0;
				position: relative;
			}
		}
</style>
</head>

<a href="/" title="На главную страницу">%%host%%</a>
<p class="copyright"><em>Интернет без цензуры</em></p>
<header id="header">
<h1>Обход блокировок</h1>
<p>Простой и удобный способ открыть вебсайт или конкретную заблокированную страницу.<br>
Просто введите URL-адрес и нажмите на кнопку. Сайт откроется в новом окне.</p>
</header>
<form id="razblokirovat" method="post" action="/" target="_blank" rel="nofollow noopener" novalidate>
<input type="url" name="url" id="sajt" value="%%url%%" placeholder="Введите адрес сайта. Например: kinozal.tv">
<input type="hidden" name="token" value="%%token%%">
<br>
<input type="submit" value="разблокировать сайт">
</form>

<footer id="footer">
<ul class="copyright">
<li>%%year%%, Sim-sim, <a href="https://github.com/stopcenz/sim-sim" title="Get source">source code</a>.</li>
</ul>
</footer>
</body></html>
"""
