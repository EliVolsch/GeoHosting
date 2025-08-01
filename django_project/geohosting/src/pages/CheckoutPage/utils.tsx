import { SalesOrder } from "../../redux/reducers/ordersSlice";
import { NavigateFunction } from "react-router/dist/lib/hooks";

export function checkCheckoutUrl(
  salesOrder: SalesOrder,
  navigate?: NavigateFunction,
) {
  // Check checkout url
  const originalUrl = location.href.replace(location.origin, "");
  let targetUrl = originalUrl;
  if (salesOrder.app_name) {
    localStorage.setItem("appName", "");
    localStorage.setItem("companyName", "");
    localStorage.setItem("companyId", "");
  }
  switch (salesOrder.order_status) {
    case "Waiting Payment":
      targetUrl = `/orders/${salesOrder.id}/payment`;
      break;
    case "Waiting Configuration":
      targetUrl = `/orders/${salesOrder.id}/configuration`;
      break;
    case "Waiting Deployment":
      targetUrl = `/dashboard/instances/${salesOrder.app_name}`;
      break;
    case "Deployed":
      targetUrl = `/dashboard/instances/${salesOrder.app_name}`;
      break;
  }
  if (navigate && originalUrl.replace("/#", "") != targetUrl) {
    navigate(targetUrl);
  }
  return targetUrl;
}
