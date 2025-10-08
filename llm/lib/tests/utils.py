import contextlib

import frappe

from llm.lib.session import Session


def print_stats(sessions: list[Session]):
	from llm.core.test_llm.utils import print_stats as print_stats_inner

	print_stats_inner([session.get_stats() for session in sessions])


def delete_sessions(sessions: list[Session]):
	for session in sessions:
		with contextlib.suppress(Exception):
			frappe.delete_doc("LLM Session", session.id, force=True)

	frappe.db.commit()
